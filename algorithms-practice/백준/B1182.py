# 백준 1182 : 부분수열의 합
import sys; input=sys.stdin.readline
n,s = map(int, input().strip().split())
aList = [0] + list(map(int,input().strip().split()))
preFix = [0]*(n+1)
cnt = 0
for i in range(1, n+1):
    preFix[i] = preFix[i-1] + aList[i]
for i in range(n):
    for j in range(i+1, n+1):
        if preFix[j] - preFix[i] == s:
            cnt += 1
print(cnt)