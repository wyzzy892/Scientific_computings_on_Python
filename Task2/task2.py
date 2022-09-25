import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10.0, 50)

fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.set(title='(а)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\sin{(x)}$')
ax_2.set(title='(б)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\cos{(x)}$')
ax_3.set(title='(в)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\sin^2{(x)}$')
ax_4.set(title='(г)', xlim=(-1.0, 11.0), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$x^{0.15}$')

ax_1.plot(x, np.sin(x), 'ko-', label='1')
ax_2.plot(x, np.cos(x), 's-', color='orange', linewidth=1, markersize=3.0, label='2')
ax_3.plot(x, (np.sin(x))**2, '^-', color='magenta', linewidth=1, label='3')
ax_4.plot(x, (x)**0.15, '--', linewidth=1, label=r'$x^2$')

fig.tight_layout()
plt.show()