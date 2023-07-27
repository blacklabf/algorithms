# SWEA 1945 : 간단한 소인수분해
import sys; input = sys.stdin.readline
t = int(input())
nList = [2, 3, 5, 7, 11]
for i in range(1,t+1):
    ans = []
    n = int(input())
    for num in nList:
        cnt = 0 
        while n % num == 0:
            n = n //num
            cnt += 1
        ans.append(cnt)
    print('#{}'.format(i), *ans, sep=' ')