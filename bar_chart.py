import matplotlib.pyplot as plt

# Data
x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 3, 8, 4]

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar graph")

# Bar chart
plt.bar(x, y, color='skyblue')

# Display
plt.show()
