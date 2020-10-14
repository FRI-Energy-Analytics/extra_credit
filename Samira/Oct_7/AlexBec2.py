import math
a = float(input())
b = float(input())
# pythagorean theorem
hy = ((a**2 + b ** 2) ** (.5)) / 2
# definition of arc tangent
A = math.atan(a/b)
# law of cosines
MB = (b**2 + hy**2 - (2*b*hy*math.cos(A)))**.5
# law of sines
mbc = math.asin(((hy) * math.sin(A)) / (MB))
# definition of radian to degrees
print(str(round(mbc * (180 / math.pi))) + "\u00B0")