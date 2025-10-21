import sys
input = sys.stdin.readline

n = int(input())  # 총 금액
t = int(input())  # 항목 수

total = 0  # 합계는 숫자로 누적

for i in range(t):
    x, y = map(int, input().split())
    total += x * y  # 항목 가격 × 개수를 누적

if n == total:
    print("Yes")
else:
    print("No")