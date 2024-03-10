# SWEA 1926 : 간단한 369게임
import sys ; input = sys.stdin.readline
n = int(input())
aList = [i for i in range(1,n+1)]
bList = ['3','6','9']

for i in aList:
    cnt = 0
    num = str(i)
    for j in num:
        if j in bList:
            cnt += 1
    if cnt == 0:
        print(num, end=' ')
    else:
        print('-'*cnt, end=' ')





