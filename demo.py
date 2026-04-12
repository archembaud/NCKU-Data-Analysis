import matplotlib.pyplot as plt

# Your data
A = [5, 5, 4, 3, 5, 6, 4, 3]

# Create histogram
plt.hist(A, bins=range(min(A), max(A) + 2), edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of List A')

# Show plot
plt.show()
