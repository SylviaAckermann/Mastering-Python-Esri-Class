
nums = list(range(10))

print(nums)

even_nums = []

for num in nums: 
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)

uneven_nums = [num for num in nums if num % 2 == 1]
print(uneven_nums)