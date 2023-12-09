import matplotlib.pyplot as plt

# # Using the Seaborn style
# plt.style.use('seaborn-v0_8')

# # Creating a scatter plot with multiple points
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.scatter(input_values, squares, s=100)  # Increased point size for visibility

# # Setting chart title and labeling axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # Setting the size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)

# # Showing the plot
# plt.show()

# # Saving the plot to a file
# fig.savefig('scatter_plot.png')



x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Setting the size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Showing the plot
plt.show()

# Saving the plot to a file
fig.savefig('scatter_plot.png')