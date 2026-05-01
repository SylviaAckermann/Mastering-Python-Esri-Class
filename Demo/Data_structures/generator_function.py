

def colors():
    print("in the colors1 function")
    yield "red"

    print("in the colors2 function")
    yield "green"

    print("in the colors3 function")
    yield "blue"


for color in colors():
    print("in the for loop")
    print(color)

print("-----")

colors_iter = iter(colors())
colors_iter2 = iter(colors())
color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)
color2 = next(colors_iter2)
print(color2)