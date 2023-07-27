# SWEA 1285 : 아름이의 돌 던지기
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    ans = []
    n = int(input())
    location = list(map(int,input().strip().split()))
    for j in range(n):
        ans.append(abs(location[j]))
    print('#{} {} {}'.format(i,min(ans),ans.count(min(ans))))