# 백준 11723 : 집합
# pypy3 : 시간을 줄이지만 메모리가 큼
import sys; input = sys.stdin.readline

m = int(input())
S = set() # 집합선언 

for i in range(m):
    aList = list(input().strip().split())
    a = aList[0]
    if len(aList) >= 2:
        b = int(aList[1])

    if a == 'add':
        S.add(b)
    elif a == 'remove':
        if b in S:
            S.remove(b)
    elif a == 'check':
        if b in S:
            print(1)
        else: print(0)
    elif a == 'toggle':
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif a == 'all':
        S = set([i for i in range(1, 21)])
    elif a == 'empty':
        S = set()
        
