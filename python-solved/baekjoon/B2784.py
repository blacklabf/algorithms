# 백준 피보나치 수2
import sys; input = sys.stdin.readline
n = int(input())

d = [0] * 91

d[0] = 0
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
