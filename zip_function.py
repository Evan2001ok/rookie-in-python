x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for x in zip(labels, x_coord, y_coord, z_coord):
    points.append(f"{x[0]}: {x[1]}, {x[2]}, {x[3]}")

for point in points:
    print(point)
