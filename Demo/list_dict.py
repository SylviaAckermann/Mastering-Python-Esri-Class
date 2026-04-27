
nums = [1,2,3,4,5]

print(type(nums))
print(nums)

nums.append(10)
for num in nums:
    print(num)

print(f"Length of numbs: {len(nums)}")

people = [{"fn": "Bob", "ln": "Smith", "age": 23},
          {"fn": "Alice", "ln": "Timmons", "age": 30},
          {"fn": "Catherine", "ln": "Jones", "age": 21}]

for person in people:
    print(type(person))
    print(person)

people.append({"fn": "Philipp", "ln": "Hut", "age": 34})
print(people)
