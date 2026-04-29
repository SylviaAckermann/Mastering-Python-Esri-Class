
class Person:

    def __init__(self, fn, ln, age, city):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.city = city

    def walk(self):
        print(f"{self.fn} is walking")
    
    def run(self):
        print(f"{self.fn} is running")
    
    def hide(self):
        print(f"{self.fn} is playing hide and seek")

    def greet(self):
        print(f"Hi, I'm {self.fn} {self.ln}, I'm {self.age} years old and live in {self.city}.")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
        
    def print_adult(self, is_adult):
        if is_adult:
            print(f"{self.fn} is an adult.")
        else:
            print(f"{self.fn} is a child.")