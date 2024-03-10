# SWEA 1208 : Flatten
import sys ; input =sys.stdin.readline
for i in range(1,11):
    t = int(input())
    height = list(map(int,input().strip().split()))
    for j in range(100):
        Midx = height.index(max(height))
        Nidx = height.index(min(height))
        height[Midx] -=1
        height[Nidx] +=1
    print('#{} {}'.format(t,max(height)-min(height)))