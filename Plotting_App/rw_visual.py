import matplotlib.pyplot as plt
from random_walk import RabdomWalk

#Making a random walk.
rw = RabdomWalk()
rw.fill_walk()

#Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()