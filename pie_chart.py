import matplotlib.pyplot as plt

fruits = ["Apple", "Orange", "Grape", "Watermelon"]
price = [20, 60, 10, 80]

plt.pie(price, labels=fruits, autopct="%.1f%%")
plt.title("Pie Grsph")
plt.show()
