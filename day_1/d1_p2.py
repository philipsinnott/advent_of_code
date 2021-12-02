import requests

input = open("input.txt")

input = input.read()
input = input.splitlines()
integer_map = map(int, input)
input = list(integer_map)

# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

counter = 0
# loop through list of values, set start pos to the first index of the "second sliding window"
for i in range(3, len(input)):
    if input[i] > input[i - 3]:
        counter += 1
print(counter)

# for i in range(3, len(input)):
#     print(input[i])
#     print(input[i - 3])
#
#     if input[i] > input[i - 3]:
#         print(True)
#         # 6 true i rad, sedan 2 falska
#     else:
#         print(False)