import numpy as np

a = np.array([1, 2, 3, 4, 5, 7])
print(a)

b = np.arange(2, 10, 2)
print(b)

c = np.linspace(0, 10, 6)
print(c)

d = np.array([[1, 2, 3], [4, 5, 6]])
print(d[0, 0])
print(d[1, 2])

e = np.zeros((2, 3))
print(e)

f = np.ones((2, 3))
print(f)

g = np.random.random((2, 3))
print(g)

print(d+f)
print(c*2)
print(f.T)

print(c > 3)
print(a[2:]) #slajszowanie

print(g.sum())
print(g.min())
print(g.max())
print(g.mean())

