# SWEA 1206 : 1일차 - view
import sys; input = sys.stdin.readline

for t in range(1,11):
    n = int(input())
    nList = [0] + list(map(int,input().strip().split()))
    ans = [0] * (n+1)
    for i in range(2,n-1):
        a = nList[i] - nList[i-1]
        b = nList[i] - nList[i-2] 
        c = nList[i] - nList[i+1]
        d = nList[i] - nList[i+2]
        if a >= 0 and b >= 0 and c >= 0 and d >= 0 :
            ans[i] = min(a,b,c,d)
    print('#{} {}'.format(t,sum(ans)))


