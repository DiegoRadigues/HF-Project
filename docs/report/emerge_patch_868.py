import emerge as em
import numpy as np
from emerge.plot import plot_sp, smith, plot_ff_polar, plot_ff

""" PATCH ANTENNA DEMO – version LoRa 868 MHz - FR4

Adaptation du modèle patch 1.575 GHz vers ~868 MHz.
Substrat FR4 (εr ≈ 4.4), patch rectangulaire LoRa EU 868 MHz.
"""

# --- Unit and simulation parameters --------------------------------------
mm = 0.001              # meters per millimeter

# --- Antenna geometry dimensions ----------------------------------------
# Patch dimensions pour viser ~868 MHz
Wpatch = 105 * mm       # patch width
Lpatch = 82.3 * mm      # patch length

# Microstrip feed line pour ~50 Ω sur h ≈ 1.6 mm
wline = 3.1 * mm        # feed line width (~50 Ω sur FR4 1.6 mm)

# Inset feed : profondeur ~0.3 * Lpatch
wstub = 9 * mm          # stub width (un peu plus large que la ligne)
lstub = 0.3 * Lpatch    # stub (feed) length

# Substrat
wsub = 180 * mm         # substrate width
hsub = 180 * mm         # substrate length
th  = 1.6 * mm          # substrate thickness

# Airbox : rayon au moins λ/4 autour de l’antenne (λ ≈ 0.345 m à 868 MHz)
Rair = 220 * mm         # air sphere radius

# Plage de fréquences : recentrée autour de 863–870 MHz
f1 = 0.84e9             # 840 MHz
f2 = 0.90e9             # 900 MHz

# --- Create simulation object -------------------------------------------
model = em.Simulation('PatchAntenna_868MHz')
model.check_version("1.2.2")  # Checks version compatibility.

# --- Define geometry primitives -----------------------------------------
dielectric = em.geo.Box(
    wsub, hsub, th,
    position=(-wsub/2, -hsub/2, -th)
)

air = em.geo.Sphere(Rair).background()

rpatch = em.geo.XYPlate(
    Wpatch, Lpatch,
    position=(-Wpatch/2, -Lpatch/2, 0)
)

ground = em.geo.XYPlate(
    wsub, hsub,
    position=(-wsub/2, -hsub/2, -th)
).set_material(em.lib.PEC)

# --- FEED INSET correctement aligné -------------------------------------
line_x0 = -wline/2
line_y0 = -Lpatch/2

cutout1 = em.geo.XYPlate(
    wstub, lstub,
    position=(line_x0 - wstub, line_y0, 0)
)
cutout2 = em.geo.XYPlate(
    wstub, lstub,
    position=(line_x0 + wline, line_y0, 0)
)

line = em.geo.XYPlate(
    wline, lstub,
    position=(line_x0, line_y0, 0)
)

# Patch final : encoche + ligne
rpatch = em.geo.remove(rpatch, cutout1)
rpatch = em.geo.remove(rpatch, cutout2)
rpatch = em.geo.add(rpatch, line)
rpatch.set_material(em.lib.PEC)

# Port : de la masse au patch, centré sur la ligne
port = em.geo.Plate(
    np.array([line_x0, line_y0, -th]),  # lower port corner (ground)
    np.array([wline, 0, 0]),            # width along X
    np.array([0, 0, th])                # height along Z up to patch
)

# --- Assign materials and simulation settings ---------------------------
dielectric.material = em.Material(4.4, color="#207020", opacity=0.9)

# Mesh resolution
model.mw.set_resolution(0.25)

# Frequency sweep recentré (assez fin pour voir le creux)
model.mw.set_frequency_range(f1, f2, 61)

# --- Combine geometry into simulation -----------------------------------
model.commit_geometry()

# --- Mesh refinement settings -------------------------------------------
model.mesher.set_boundary_size(rpatch, 3 * mm)
model.mesher.set_face_size(port, 0.5 * mm)

# --- Generate mesh and preview ------------------------------------------
model.generate_mesh()
model.view(selections=[port], plot_mesh=True)

# --- Boundary conditions -------------------------------------------------
port_bc = model.mw.bc.LumpedPort(
    port, 1,
    width=wline, height=th,
    direction=em.ZAX, Z0=50
)

boundary_selection = air.boundary()
pec_selection = em.select(rpatch, ground)

abc = model.mw.bc.AbsorbingBoundary(boundary_selection)

# --- Run frequency-domain solver ----------------------------------------
model.view(plot_mesh=True, volume_mesh=False)
data = model.mw.run_sweep()

# --- Post-process S-parameters ------------------------------------------
freqs = data.scalar.grid.freq
S11 = data.scalar.grid.model_S(1, 1, freqs)

plot_sp(freqs, S11)
smith(S11, f=freqs, labels='S11')

S11_dB = 20 * np.log10(np.abs(S11))
idx_min = np.argmin(S11_dB)
f_res = freqs[idx_min]
print("Fréquence de résonance estimée : %.2f MHz" % (f_res/1e6))
print("S11_min = %.1f dB" % S11_dB[idx_min])

# --- Far-field radiation pattern à 868 MHz ------------------------------
ff1 = data.field.find(freq=0.868e9) \
    .farfield_2d((0, 0, 1), (1, 0, 0), boundary_selection)
ff2 = data.field.find(freq=0.868e9) \
    .farfield_2d((0, 0, 1), (0, 1, 0), boundary_selection)

plot_ff(
    ff1.ang * 180 / np.pi,
    [ff1.normE / em.lib.EISO, ff2.normE / em.lib.EISO],
    dB=True, ylabel='Gain [dBi]'
)

plot_ff_polar(
    ff1.ang,
    [ff1.normE / em.lib.EISO, ff2.normE / em.lib.EISO],
    dB=True, dBfloor=-20
)

# --- 3D radiation visualization -----------------------------------------
model.display.add_object(rpatch)
model.display.add_object(dielectric)

field = data.field.find(freq=0.868e9)
ff3d = field.farfield_3d(boundary_selection)
surf = ff3d.surfplot('normE', rmax=120 * mm,
                     offset=(0, 0, 40 * mm))

model.display.add_surf(*surf)
model.display.show()
