import numpy as np

# https://www.jessicayung.com/numpy-arrays-memory-and-strides/
# create a simple array
X = np.array([[0, 1, 2], [3, 4, 5]], dtype="int16")

print(X)
print("Strides ", X.strides)
# should get (6, 2)
# why? there are 2 bits per row and 3 rows (3x2=6)
print("X[1, 1]=", X[1, 1])  # should get 4
offset = sum(X.strides * np.array((1, 1)))
print("offset / X.itemsize =", offset / X.itemsize)

# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html
# y = np.reshape(np.arange(2 * 3 * 4), (2, 3, 4))
# print(y)

