import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

energia = np.loadtxt("results.e.out")
fuerzas = np.loadtxt("results.f.out")
E_real, E_pred = energia[:,0], energia[:,1]
Fx_real, Fy_real, Fz_real = fuerzas[:,0], fuerzas[:,1], fuerzas[:,2]
Fx_pred, Fy_pred, Fz_pred = fuerzas[:,3], fuerzas[:,4], fuerzas[:,5]

plt.rcParams.update({"font.family": "DejaVu Sans", "axes.linewidth": 1.1})
color_points = "#1f77b4"; color_fit = "#003f5c"; color_ref = "#777777"

plt.figure(figsize=(7,6))
plt.scatter(E_real, E_pred, color=color_points, alpha=0.45, s=20)
plt.plot([E_real.min(), E_real.max()], [E_real.min(), E_real.max()], '--', color=color_ref)
coef = np.polyfit(E_real, E_pred, 1); poly_fit = np.poly1d(coef)
plt.plot(E_real, poly_fit(E_real), color=color_fit, linewidth=2)
eq_text = f"$y = {coef[0]:.3f}x + {coef[1]:.3f}$"
plt.text(0.05, 0.93, eq_text, transform=plt.gca().transAxes, fontsize=11, color=color_fit)
plt.xlabel("Energía real (eV)"); plt.ylabel("Energía predicha (eV)")
plt.tight_layout(); plt.show()
