import math
AB = float(input())
BC = float(input())

output = math.atan(AB/BC)
print("{}°".format(round(math.degrees(output))))