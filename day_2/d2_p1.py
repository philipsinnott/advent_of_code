# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

x = 0 # horizontal pos
y = 0 # vertical pos

# # Example
# x += 5
# y += 5
# x += 8
# y -= 3
# y += 8
# x += 2
# print(f'Pos: {x}, {y}')
# print(x*y)

data = open("input.txt")
data = data.read()
data = list(data.splitlines())

for direction in data:
    if direction.__contains__("forward"):
        x += int(direction[-1])
    if direction.__contains__("down"):
        y += int(direction[-1])
    if direction.__contains__("up"):
        y -= int(direction[-1])
print(f'{x}, {y}')

# What do you get if you multiply your final horizontal position by your final depth?
print(x*y)