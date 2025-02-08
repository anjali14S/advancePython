import numpy as np

# declare a list

a = [1, 2, 3, 4, 5]
print(f" variable a : {a}, Type : { type(a)}")

# create a numpy array:
b = np.array(a)
print(f"variable b : {b}, Type: {type(b)}")

print(b.ndim)
print(b.shape)