import sys
input = sys.stdin.readline

h, m = map(int, input().split())
t = int(input())

h += (m+t)//60
h = (h) % 24
print(h, (m+t) % 60)