import requests

input = open("input.txt")

input_content = input.read()
input_content = input_content.splitlines()
integer_map = map(int, input_content)
input_content = list(integer_map)

# How many measurements are larger than the previous measurement?
larger_than_previous = []

for i, val in enumerate(input_content):
    if i != 0:
        if val > input_content[i - 1]:
            larger_than_previous.append(i)
print(len(larger_than_previous))