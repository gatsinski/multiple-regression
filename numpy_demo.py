import numpy as np

y = np.array([31.4, 14.6, 6.4, 28.3, 42.1, 15.3])
X = np.array([
  [345, 168, 94, 187, 621, 255],
  [65, 18, 0, 185, 87, 0],
  [23, 18, 0, 98, 10, 0],
])

X = X.T  # transpose so input vectors are along the rows
X = np.c_[X, np.ones(X.shape[0])]  # add bias term
result = np.linalg.lstsq(X, y, rcond=None)[0]
print(result)
