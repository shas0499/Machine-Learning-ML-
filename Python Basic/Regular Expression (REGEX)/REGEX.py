import re

match = re.search(r"World", "Hello World")
if match:
    print("Match found anywhere in the string.")

print(re.match('abc','abcde'))

numbers = re.findall(r"\d+", "The year is 2025 and the month is 11.")
print(numbers)

new_string = re.sub(r"Java", "Python", "I love Java programming.")
print(new_string)