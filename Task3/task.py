import numpy as np
import scipy as sp

# определяем подыинтегральную функцию
def f(x):
    return 1/np.cos(x)

# вычисляем определенный интеграл при помощи метода quad
print(sp.integrate.quad(f, 0.0, np.pi/4)[0])

# вычисление решения, полученного при ручном счете интеграла
print(np.log(2.0/np.sqrt(2)+1.0))