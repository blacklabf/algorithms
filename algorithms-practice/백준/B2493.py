# 백준 탑 - 스택
import sys ; input = sys.stdin.readline
n = int(input())
top = list(map(int, input().strip().split())) # top = [ 6 9 5 7 4]
ans = [0] * n
for i in range(n-1, 1, -1): # 4 3 2 1
    if top[i] < min(top[:i-1]):
        pass
    else :
        
        top.index()