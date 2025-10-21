import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if b < 45:
    a = (a - 1) % 24 
    b += 60
print(a, b - 45)