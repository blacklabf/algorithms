# 백준 회의실배정
import sys ; input = sys.stdin.readline
from itertools import combinations

n = int(input())
nList = [list(map(int, input().split())) for _ in range(n)]
mList = []
for i in range(n):
    rn = list(range(nList[i][0], nList[i][1]+1))
    mList.append(rn)
combi = list(combinations(mList, ))
for j in range(n):

