# 백준 2579 : 계단오르기 (DP)
# 1칸 혹은 2칸 / 연속해서 3칸은 안됨 / 시작점은 치지 않음 / 최댓값 구함

import sys ; input = sys.stdin.readline
n = int(input())
nList = [int(input()) for _ in range(n)]
mList = nList[::-1]
start = mList[0] # 마지막 무조건 밟음 


max(mList[i], mList[i+1])
    

