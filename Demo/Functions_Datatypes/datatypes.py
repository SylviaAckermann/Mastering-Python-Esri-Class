

t = "hello"
print(t)
print(type(t))

s = 2
print(s)
print(type(s))

r = 2.4
print(r)
print(type(r))

p = True
print(p)
print(type(p))

name = input("Enter your name: ")
print("Hello, "+name+"!")

age_input = input("Enter your age: ")
age = int(age_input)
print(type(age), age)

age_input = age_input + str(1)   # 261 => opterator overloading
age = age + 1                    # 27
print(age_input)
print(age)