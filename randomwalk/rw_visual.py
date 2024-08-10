import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)
ax.set_aspect("equal")

ax.scatter(0, 0, c="green", edgecolors="none", s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()