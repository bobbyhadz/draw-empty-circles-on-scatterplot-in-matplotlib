# How to draw empty circles on a Scatter Plot in Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(90)
y = np.random.randn(90)

print(x)

plt.scatter(x, y, s=80, edgecolors='r', facecolors='none')
plt.show()