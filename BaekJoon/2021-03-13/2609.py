import math
import sys

a,b = map(int, sys.stdin.readline().split())

a_b_gcd = math.gcd(a,b)
a_b_lcm = int(a * b / a_b_gcd)

print(a_b_gcd)
print(a_b_lcm)