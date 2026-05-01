

nums = [0,1,2,3,4]

for num in nums:
    print(num)
    # Challenge: If nums gets a long list, it would take up lot of memory

print("---------")

for num in range(5):
    print(num)
    # Range utilizes memory better, num object is generated seperately per iteration

print(range(5))
print(list(range(5)))