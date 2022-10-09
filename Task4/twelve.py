from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def f(y, x):
    return -2.5*y

xi = np.linspace(0, 1, 50)
y0 = 0
numeric_solution = integrate.odeint(f, y0, xi)
exact_soluion = np.zeros(xi.size)
err = np.abs(exact_soluion-numeric_solution[:, 0])
for i in err:
    print("{0:.25f}".format(i))

fig = plt.figure(figsize=(14, 5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set_ylim(-0.02, 0.02)
ax2.set_ylim(-0.02, 0.02)
ax1.plot(xi, exact_soluion, 'k', linewidth=3, label='точн.')
ax1.plot(xi, numeric_solution[:, 0], ':y', label='числ.')
ax2.plot(xi, err, 'r', linewidth=2, label='ошибка')
ax1.set_title("Графики точного и численного решений")
ax2.set_title("График ошибки")
fig.legend()
plt.show()
