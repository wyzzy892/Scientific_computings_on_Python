import numpy as np
from timeit import default_timer as timer

# 1 arrays
nums = 1000   # size of array
a1 = np.linspace(0, 100, nums, dtype=float)
a2 = np.linspace(0, 1, nums, dtype=float)
res = np.zeros(nums)

# measure time using for cycle
print("1. Массивы.")
print("Сложение напрямую в цикле for.")
start = timer()
for i in range(nums):
    res[i] = a1[i]+a2[i]
end = timer()
print(u"Время выполнения: %.3e с\n" % (end - start))

# measure time for numpy
print("Сложение с помощью NumPy.")
start = timer()
res = a1+a2
end = timer()
print(u"Время выполнения: %.3e с\n" % (end-start))

# Matrices
def fill(matr, rows=100, cols=1000):
    l = []
    for i in range(rows):
        l.append(matr[:cols])
    return np.array(l, dtype=float)

rows = 100
cols = 100
m1 = fill(a1, rows, cols)
m2 = fill(a2, rows, cols)
m_res = np.array([np.zeros(rows) for i in range(rows)])
# measure time using for cycle
print("2. Матрицы.")
print("Сложение напрямую в цикле for.")
start = timer()
for i in range(rows):
    for j in range(rows):
        for k in range(cols):
            m_res[i, j] += m1[i, k]*m2[k, j]
end = timer()
print(u"Время выполнения: %.3e с\n" % (end - start))


# measure time using numpy
print("Сложение с помощью NumPy.")
start = timer()
m_res = m1.dot(m2.T)
end = timer()
print(u"Время выполнения: %.3e с" % (end-start))