from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def f_exact(x):
    return 0.5*np.log(np.abs(2.0*x-19.0))+1.0

def f(y, t):
    x = y[0]
    v = y[1]

    f0 = v
    f1 = -2.0*v**2
    return [f0, f1]

y0 = [1.0, 1.0]
t = np.linspace(10, 20, 50)
exact_sol = f_exact(t)
sol = integrate.odeint(f, y0, t)
err = np.abs(exact_sol-sol[:, 0])

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.plot(t, exact_sol, label='точн.', color='orange', linewidth=3)
ax1.plot(t, sol[:,0], label='числ.', color='b', linestyle=':')
ax2.plot(t, err, label='ошибка')
ax1.legend()
ax2.legend()
ax1.grid()
ax2.grid()
plt.show()








