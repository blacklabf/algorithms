# SWEA 1217 : 거듭 제곱
import sys ; input = sys.stdin.readline

def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m-1)

for _ in range(1, 11):
    tc = int(input())
    a, b = map(int, input().strip().split())
    ans = power(a,b)
    print('#{} {}'.format(tc, ans))





