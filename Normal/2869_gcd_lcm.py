x,y = map(int, input().split())

def gcd(x, y):
    while y:
        x,y = y, x%y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

print(gcd(x,y))
print(lcm(x,y))

# import math
# print(math.gcd(x,y))
# print(math.lcm(x,y))