# SWEA 1970 : 쉬운 거스름돈
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    ans = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    n = int(input())
    for j in range(8):
        ans[j] = n // money[j]
        n = n % money[j]
    print('#{}'.format(i))
    print(*ans,sep=' ')