import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(loc=0, scale=1, size=1000)
plt.figure(figsize=(10, 6))  # Optional: bigger figure

# Scatter plot: x = index, y = data values
plt.scatter(range(len(data)), data, color='blue', alpha=0.6, s=10)

# Labels and title
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Scatter Plot of 1000 Random Numbers from Normal Distribution")

plt.grid(True)  # Optional: makes plot easier to read
plt.show()
