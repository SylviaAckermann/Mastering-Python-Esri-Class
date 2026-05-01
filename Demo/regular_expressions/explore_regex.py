import re

# content = "as busy as a bee"

#print(re.findall(r"b[a-z]+", content))

#r = re.compile(r"b[a-z]+")   # starts with letter b, followed by at least one more of the characters a-z
#r = re.compile(r"b[a-z]{2}") # starts with letter b, extract 2 following characters
# r = re.compile(r"\sa[a-z]*")  # starts with letter a, skip first instance and use all following once
#r = re.compile(r"as")

# match the regular expression from the start of the content
# print(r.match(content))

# searches the string for the first match
# print(r.search(content))

# returns a list of the matches
# print(r.findall(content))

# returns all matches as match objects
# print(list(r.finditer(content)))

content = "red|green;blue:yellow"

r = re.compile(r"\||;|:")   # split content by delimiter |; or :
print(r.split(content))
print(r.sub(", ", content))

# content = "red|green;blue:yellow"
# r = re.compile(r"[|;:]")
# print(r.split(content))
# print(r.sub(",", content))