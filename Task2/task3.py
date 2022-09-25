import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10.0, 50)

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0,0].set(title='(а)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\sin{(x)}$')
ax[0,1].set(title='(б)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\cos{(x)}$')
ax[1,0].set(title='(в)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\sin^2{(x)}$')
ax[1,1].set(title='(г)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$x^{0.15}$')

ax[0,0].plot(x, np.sin(x), 'k-')
ax[0,1].plot(x, np.cos(x), 'k:')
ax[1,0].plot(x, (np.sin(x))**2, 'k--')
ax[1,1].plot(x, (x)**0.15, color='gray')

fig.tight_layout()
plt.show()