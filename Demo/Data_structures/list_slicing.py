
# print letters A to Z
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(letters)

letters = [chr(i) for i in range(97,123)]
print(letters)

# print 3rd letter of alphabet
print(letters[3])

# print W, X and Y
print(letters[-4:-1])

# print first 10 letters of the alphabet by skipping overy 2nd one
print(letters[1:10:2])