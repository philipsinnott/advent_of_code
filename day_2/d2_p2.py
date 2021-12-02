x = 0 # horizontal pos
y = 0 # depth / vertical pos
aim = 0

data = open("input.txt")
data = data.read()
data = list(data.splitlines())

#     down X increases your aim by X units.
#     up X decreases your aim by X units.
#     forward X does two things:
#         *It increases your horizontal position by X units.
#         *It increases your depth by your aim multiplied by X.

for direction in data:
    if direction.__contains__("forward"):
        x += int(direction[-1])
        # if aim > 0:
        y += (aim * int(direction[-1]))
    elif direction.__contains__("down"):
        aim += int(direction[-1])
    elif direction.__contains__("up"):
        aim -= int(direction[-1])
print(f'{x}, {y}')
print(x*y)
