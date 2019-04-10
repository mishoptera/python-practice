import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simple tests
print('Hello world!')
17+25

# Print dataframe
pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# Show plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
