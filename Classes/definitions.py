
from person import Person


p1 = Person("Bob", "Smith", 32, "Munich")
print("Firstname: " + p1.fn)
print("Lastname: " + p1.ln)
print(f"Age : {p1.age}")

p1.greet()
p1.walk()
p1.print_adult(p1.is_adult())
print("----------------------")

p2 = Person("Alice", "Smith", 34, "Stuttgart")
print("Firstname: " + p2.fn)
print("Lastname: " + p2.ln)
print(f"Age : {p2.age}")

p2.greet()
p2.run()
p2.print_adult(p2.is_adult())
print("----------------------")

p3 = Person("Luna", "Smith", 4, "Redlands")
print("Firstname: " + p3.fn)
print("Lastname: " + p3.ln)
print(f"Age : {p3.age}")

p3.greet()
p3.hide()
p3.print_adult(p3.is_adult())