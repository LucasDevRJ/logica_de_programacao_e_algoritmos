x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)

x = [5, 7, 9, 11]
y = x[:] #essa cópia não altera as duas listas. Altera somente a y
print(x)
print(y)

y[0] = 2
print(x)
print(y)