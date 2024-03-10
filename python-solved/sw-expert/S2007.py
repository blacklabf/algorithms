# SWEA 2007 : 패턴 마디의 길이
import sys; input = sys.stdin.readline
t = int(input())

for i in range(1,t+1):
    nList = input().strip()
    cnt = 0
    for j in range(1,30):
        if nList[0] == nList[j]:
            




# for i in range(1,t+1):
#     nList = input().strip()
#     j = 1
#     while nList[0] != nList[j]:
#         if j == len(nList)-1 :
#             break
#         else:
#             j += 1
#     print('#{} {}'.format(i, j))        

