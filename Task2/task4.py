import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10.0, 50)

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0,0].set(title='(а)', xlabel=r'$x$', ylabel=r'$\sin{(x)}$', xlim=(0.0, 2*np.pi))
ax[0,1].set(title='(б)', xlabel=r'$x$', ylabel=r'$\cos{(x)}$', xlim=(0.0, 2*np.pi))
ax[1,0].set(title='(в)', xlabel=r'$x$', ylabel=r'$\sin^2{(x)}$', xlim=(0.0, 2*np.pi))
ax[1,1].set(title='(г)', xlabel=r'$x$', ylabel=r'$x^{0.15}$', xlim=(0.0, 2*np.pi))

ax[0,0].plot(x, np.sin(x), 'k-')
ax[0,1].plot(x, np.cos(x), 'k:')
ax[1,0].plot(x, (np.sin(x))**2, 'k--')
ax[1,1].plot(x, (x)**0.15, color='gray')

fig.tight_layout()
plt.show()