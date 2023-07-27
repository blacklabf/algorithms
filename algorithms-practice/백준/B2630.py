# 백준 2630 : 색종이 만들기
import sys; input = sys.stdin.readline
n = int(input())
arr = [[]]
newList = []
for _ in range(n):
    arr.append([' '] + list(map(int, input().strip().split())))

dx = [-1, 0, 1, 0] # 시계방향
dy = [0, 1, 0, -1]

for x in range(1, n+1):
    for y in range(1, n+1):
        newList.append(arr[x][y])

for i in range(len(newList)):
    if newList[i] == 0 and newList[i+1] == 0:
        sldkfxj;asldkgfjewhlrbk'jp
        jhiwr   
