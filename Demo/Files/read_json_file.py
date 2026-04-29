import json

class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def __repr__(self):
        return f"Person{self.__dict__}"


person = Person("Bob", "Smith")

# print(person.__dict__)

with open("person.json", "r", encoding="utf-8") as person_file:
    person_dict = json.load(person_file)
    person = Person(person_dict["fn"], person_dict["ln"])
    print(person)

# people = [
#     Person("Bob", "Smith"),
#     Person("Alice", "Smith"),
#     Person("Tim", "Smith"),
#     Person("Niki", "Smith"),
#     Person("Sam", "Smith"),
# ]

# with open("person.json", "w", encoding="utf-8") as person_file:
#     people_dicts = []
#     for person in people:
#         people_dicts.append(person.__dict__)

#     json.dump(people_dicts, person_file)