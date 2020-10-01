import re

reg_ex = re.compile(r'(?<=[a-zA-Z0-9])\W+(?=[a-zA-Z0-9])')

dimension_line = input().split(" ")
dimensions = (int(dimension_line[0]), int(dimension_line[1]))


matrix = []

for x in range(dimensions[0]):
    line = input()
    matrix.append([char for char in line])

flattened = ""

for column in range(dimensions[1]):
    for row in range(dimensions[0]):
        flattened += matrix[row][column]

print(re.sub(reg_ex, ' ', flattened))
