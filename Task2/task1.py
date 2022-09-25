import numpy as np
import matplotlib.pyplot as plt

# пользовательская переменная для хранения размера шрифта
fsize=12
# настройка типа шрифта на рисунке с помощью изменения
# записей в словаре rcParams из модуля pyplot
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
# настройка размера шрифта в различных частях рисунка
# в заголовке:
plt.rcParams['axes.titlesize'] = fsize
# в подписях осей:
plt.rcParams['axes.labelsize'] = fsize
# в подписях меток на осях:
plt.rcParams['xtick.labelsize'] = fsize
plt.rcParams['ytick.labelsize'] = fsize
# в легенде рисунка:
plt.rcParams['legend.fontsize'] = fsize

x = np.linspace(0, 10.0, 50)
x.prod()
print(x)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, np.sin(x), 'ko-', label='1')
ax.plot(x, np.cos(x), 's-', color='orange', linewidth=1, markersize=3.0, label='2')
ax.plot(x, (np.sin(x))**2, '^-', color='magenta', linewidth=1, label='3')
ax.plot(x, (x)**0.15, '--', linewidth=1, label=r'$x^2$')

ax.set_xlim(-1.0, 11.0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')

plt.show()

