import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

data = np.genfromtxt("lcurve.out", names=True)
plt.figure(figsize=(8,5))
colors = plt.cm.viridis(np.linspace(0, 1, len(data.dtype.names[1:-1])))
for i, name in enumerate(data.dtype.names[1:-1]):
    plt.plot(data['step'], data[name], label=name, color=colors[i], linewidth=2)
plt.xscale('log'); plt.yscale('log')
plt.xlabel('Step'); plt.ylabel('Loss')
plt.title('Evolución de la función de pérdida')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(frameon=False)
plt.tight_layout(); plt.show()
