
# This is a set
colors = {"red", "green", "blue"}

colors.add("brown")
colors.add("red")

print(colors)


colors = ["red", "green", "blue"]
# Capitalize letters
colors = {color.upper() for color in colors}
print(colors)

# Note: Order of sets is not consistent!!