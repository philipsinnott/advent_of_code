# Worse way of reading file
# numbers = open("test_data.txt")
# numbers = numbers.read()
# numbers = numbers.splitlines()

# Better way of reading file
with open("input.txt", "r") as data:
    numbers = [row.rstrip() for row in data]

# print(numbers)

gamma_rate = ""
binary_cols = zip(*numbers)
for col in binary_cols:
    if col.count("1") > col.count("0"):
        gamma_rate += "1"
    else:
        gamma_rate += "0"
gam = int(gamma_rate, 2) # int() function takes as second argument the base of the number to be converted, which is 2 in case of binary numbers.

epsilon_rate = ""
for bit in gamma_rate:
    if bit == "0":
        epsilon_rate += "1"
    else:
        epsilon_rate += "0"
eps = int(epsilon_rate, 2)

print(f"Power consumption: {gam * eps}")