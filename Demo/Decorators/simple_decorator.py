
TAP_INTENSITY = 2

def tap(move):
    def tap_move_fn(x):
        print("insider def_move_tap")
        result = move(x, TAP_INTENSITY)
        print("called move function")
        return result
    return tap_move_fn

@tap  # Decorator
def left(a,b):
    return a - b

@tap
def right(a,b):
    return a + b

# Option 1: Traditional nested Function
# tap_left = tap(left)
# tap_right = tap(right)


# Option 2: using Decorator
print(left(2))
print(right(3))

