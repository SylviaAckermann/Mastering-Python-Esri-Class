
def outer(func):
    print("outer")

    def inner(msg2):
        print("inner")
        func(msg2)

    return inner

def cool(msg):
    print(msg)

fn = outer(cool)
fn("fun")


def double(x):
    return x * 2

nums = range(10)

double_nums = list(map(double, nums))
print(double_nums)

double_nums = list(map(lambda x: x * 2, nums))
print(double_nums)