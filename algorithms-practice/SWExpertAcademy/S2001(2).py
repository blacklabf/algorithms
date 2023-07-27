# SWEA 2001 : 파리퇴치 (함수 이용)
import sys; input = sys.stdin.readline

def tmp(a, b):
    aSum = 0
    for i in range(a, a+m):
        for j in range(b, b+m):
            aSum += graph[i][j]
    return aSum



tc = int(input())
answer = 0
for t in range(1, tc+1):
    n , m = map(int, input().strip().split())
    graph = [list(map(int,input().strip().split())) for _ in range(n)]

    for a in range(n-m+1):
        for b in range(n-m+1):
            answer = max(answer,tmp(a,b))

    print('#{} {}'.format(t, answer))


