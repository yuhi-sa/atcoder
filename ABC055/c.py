import math
N = int(input())

power = math.factorial(N)%(pow(10,9)+7)

print(power)