import emerge as em
import numpy as np
from emerge.plot import plot_sp, smith, plot_ff_polar, plot_ff

""" PATCH ANTENNA DEMO – version LoRa 868 MHz - version 1 à valider en séance

Adaptation du modèle patch 1.575 GHz vers ~868 MHz.
Dimensions basées sur un substrat type Rogers 4003C (εr ≈ 3.38),
et un patch rectangulaire pour LoRa EU 868 MHz.

"""

# --- Unit and simulation parameters --------------------------------------
mm = 0.001              # meters per millimeter

# --- Antenna geometry dimensions ----------------------------------------
# Patch dimensions pour ~868 MHz
Wpatch = 95 * mm        # patch width (≈ 90–100 mm)
Lpatch = 75 * mm        # patch length (≈ 70–80 mm)

# Microstrip feed line pour ~50 Ω sur h ≈ 1.6 mm, εr ≈ 3.3–3.8
wline = 4.0 * mm        # feed line width (~3.5–4.5 mm)

# Inset feed : on garde le même ratio que le design 1.575 GHz (~0.3 * Lpatch)
wstub = 9 * mm          # stub width (un peu plus large que la ligne)
lstub = 0.3 * 75 * mm   # stub (feed) length ≈ 22.5 mm

# Substrat plus grand pour 868 MHz
wsub = 180 * mm         # substrate width  (150–200 mm)
hsub = 180 * mm         # substrate length (150–200 mm)
th  = 1.6 * mm          # substrate thickness (~1.6 mm)

# Airbox : rayon au moins λ/4 autour de l’antenne
# λ ≈ 0.345 m → Rair 200–250 mm
Rair = 220 * mm         # air sphere radius

# Plage de fréquences adaptée à LoRa 868 MHz
f1 = 0.84e9             # start frequency (840 MHz)
f2 = 0.90e9             # stop frequency  (900 MHz)

# --- Create simulation object -------------------------------------------
model = em.Simulation('PatchAntenna_868MHz')

model.check_version("1.2.2") # Checks version compatibility.

# --- Define geometry primitives -----------------------------------------
# Substrate block centered at origin in XY, thickness in Z (negative down)
dielectric = em.geo.Box(wsub, hsub, th,
                        position=(-wsub/2, -hsub/2, -th))

# Air box above substrate (Z positive)
air = em.geo.Sphere(Rair).background() 
# Background makes sure no materials of overlapping domains are overwritten

# Metal patch rectangle on top of substrate
rpatch = em.geo.XYPlate(Wpatch, Lpatch,
                        position=(-Wpatch/2, -Lpatch/2, 0))

ground = em.geo.XYPlate(wsub, hsub,
                        position=(-wsub/2, -hsub/2, -th)).set_material(em.lib.PEC)

# Define cutouts for inset feed: two rectangular plates to subtract
cutout1 = em.geo.XYPlate(wstub, lstub,
                         position=(-wline/2 - wstub, -Lpatch/2, 0))
cutout2 = em.geo.XYPlate(wstub, lstub,
                         position=( wline/2, -Lpatch/2, 0))

# Feed line plate to add back between cutouts
line = em.geo.XYPlate(wline, lstub,
                      position=(-wline/2, -Lpatch/2, 0))

# Plate defining lumped port geometry (origin + width/height vectors)
port = em.geo.Plate(
    np.array([-wline/2, -Lpatch/2, -th]),  # lower port corner
    np.array([wline, 0, 0]),               # width vector along X
    np.array([0, 0, th])                   # height vector along Z
)

# Build final patch shape: subtract cutouts, add feed line
rpatch = em.geo.remove(rpatch, cutout1)
rpatch = em.geo.remove(rpatch, cutout2)
rpatch = em.geo.add(rpatch, line)
rpatch.set_material(em.lib.PEC)

# --- Assign materials and simulation settings ---------------------------
# Dielectric material (Rogers 4003C-like)
dielectric.material = em.Material(3.38, color="#207020", opacity=0.9)

# Mesh resolution: un peu moins dense que pour 1.6 GHz
# (on relâche de 0.2 à 0.25)
model.mw.set_resolution(0.25)

# Frequency sweep across LoRa band
model.mw.set_frequency_range(f1, f2, 3)

# --- Combine geometry into simulation -----------------------------------
model.commit_geometry()

# --- Mesh refinement settings -------------------------------------------
# Finer boundary mesh on patch edges for accuracy
model.mesher.set_boundary_size(rpatch, 3 * mm)
# Refined mesh on port face for excitation accuracy
model.mesher.set_face_size(port, 0.5 * mm)

# --- Generate mesh and preview ------------------------------------------
model.generate_mesh()                             # build the finite-element mesh
model.view(selections=[port], plot_mesh=True)     # show the mesh around the port

# --- Boundary conditions ------------------------------------------------
# Define lumped port with specified orientation and impedance
port_bc = model.mw.bc.LumpedPort(
    port, 1,
    width=wline, height=th,
    direction=em.ZAX, Z0=50
)

# Predefining selection
# The outside of the air box for the absorbing boundary
boundary_selection = air.boundary()
# The patch and ground surface for PEC
pec_selection = em.select(rpatch, ground)

# Assigning the boundary conditions
abc = model.mw.bc.AbsorbingBoundary(boundary_selection)

# --- Run frequency-domain solver ----------------------------------------
model.view(plot_mesh=True, volume_mesh=False)

data = model.mw.run_sweep()

# --- Post-process S-parameters ------------------------------------------
freqs = data.scalar.grid.freq
freq_dense = np.linspace(f1, f2, 1001)
S11 = data.scalar.grid.model_S(1, 1, freq_dense)   # reflection coefficient

plot_sp(freq_dense, S11)                           # plot return loss in dB
smith(S11, f=freq_dense, labels='S11')             # Smith chart of S11

# --- Far-field radiation pattern ----------------------------------------
# Extract 2D cuts at phi=0 planes and plot E-field magnitude
ff1 = data.field.find(freq=0.868e9)\
    .farfield_2d((0, 0, 1), (1, 0, 0), boundary_selection)
ff2 = data.field.find(freq=0.868e9)\
    .farfield_2d((0, 0, 1), (0, 1, 0), boundary_selection)

plot_ff(ff1.ang*180/np.pi,
        [ff1.normE/em.lib.EISO, ff2.normE/em.lib.EISO],
        dB=True, ylabel='Gain [dBi]')                # linear plot vs theta

plot_ff_polar(ff1.ang,
              [ff1.normE/em.lib.EISO, ff2.normE/em.lib.EISO],
              dB=True, dBfloor=-20)                  # polar plot of radiation

# --- 3D radiation visualization -----------------------------------------
# Add geometry to 3D display
model.display.add_object(rpatch)
model.display.add_object(dielectric)

# Compute full 3D far-field and display surface colored by |E|
field = data.field.find(freq=0.868e9)
ff3d = field.farfield_3d(boundary_selection)
surf = ff3d.surfplot('normE', rmax=120 * mm,   
                     offset=(0, 0, 40 * mm))

model.display.add_surf(*surf)
model.display.show()
