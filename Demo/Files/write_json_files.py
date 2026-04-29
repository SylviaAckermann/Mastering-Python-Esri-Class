import json

class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln


person = Person("Bob", "Smith")
print(person.__dict__)

with open("person.json", "w", encoding="utf-8") as person_file:
    json.dump(person.__dict__, person_file)
    print(f"Written {person.fn} to person.json file.")

people = [
    Person("Bob", "Smith"),
    Person("Alice", "Smith"),
    Person("Tim", "Smith"),
    Person("Niki", "Smith"),
    Person("Sam", "Smith"),
]

with open("people.json", "w", encoding="utf-8") as person_file:
    people_dicts = []
    for person in people:
        people_dicts.append(person.__dict__)
        print(person.__dict__)

    json.dump(people_dicts, person_file)
    print("Written people.json file.")