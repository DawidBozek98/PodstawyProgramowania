



x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

# Check the location of the point
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin.")
elif x == 0:
    print(f"Point P({x},{y}) is on the y-axis.") # leży na prostej x
elif y == 0:
    print(f"Point P({x},{y}) is on the x-axis.") # leży na prostej y
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")
