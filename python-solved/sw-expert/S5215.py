# SWEA 5215 : 햄버거 다이어트
# dictionary 2개로 재료에 대한 score와 cal 받기
import sys; input = sys.stdin.readline
scoreDic = {}
calDic = {}

test = int(input())
for tc in range(1, test+1):
    num, limCal = map(int, input().strip().split())
    for i in range(num):
        score, cal = map(int,input().strip().split())
        scoreDic[i] = score
        calDic[i] = cal
    score의 합이 가장 높지만 cal의 합은 limcal보다 작거나 같아야 함
    