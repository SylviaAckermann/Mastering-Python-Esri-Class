"""regex capture groups demo"""

import re

# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"<b>(?P<data>.*?)</b>")

# content = "cool 45 test"
# r = re.compile(r"(?P<str1>.*? ())")


# for match in r.finditer(content):
#     print(match.groups())
#     print(match.groupdict())


# write a regular expression and code, which extracts the command name and operand

example1 = "add 2"
example2 = "multiply 3"
examples = [example1, example2]

# after the extraction create a dictionary like this

# Example 1 output: { "op_name": "add", "op_value": 2.0 }
# Example 2 output: { "op_name": "multiply", "op_value": 3.0 }

r = re.compile(r"(?P<op_name>\w+) (?P<op_value>\d+)")

for ex in examples:
    for match in r.finditer(ex):
        d = match.groupdict()
        d['op_value'] = float(d['op_value'])
        print(d)
r = re.compile(" ")


