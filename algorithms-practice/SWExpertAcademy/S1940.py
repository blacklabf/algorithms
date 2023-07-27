# SWEA 1940 : 가랏! RC카!
import sys ; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    n = int(input())
    speed = 0
    dis = 0
    for j in range(n):
        aList = list(input().strip().split())
        # if len(aList) == 0:
        #     pass
        if aList[0] == '2':
            speed = speed - int(aList[1])
            if speed <= 0:
                speed = 0
        elif aList[0] == '1':
            speed += int(aList[1])
        dis += speed
        print(dis)
    print('#{} {}'.format(i,dis))
        



    #     a, b = map(int,input().strip().split())
    #     if a == 1:
    #         speed = speed - b
    #         if speed <= 0:
    #             speed = 0
    #     elif a == 2:
    #         speed += b
    #     elif a == 0:
    #         pass
    #     dis += speed
    # print('#{} {}'.format(i,dis))
