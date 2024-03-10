# 백준 14696 : 딱지놀이
import sys; input = sys.stdin.readline

# 별(4) > 동그라미(3) > 네모(2) > 세모(1)
round = int(input()) # 딱지놀이의 라운드수

# sol1 : count
for i in range(round):
    aList = (list(map(int, input().strip().split())))
    bList = (list(map(int, input().strip().split())))
    arList = [aList[1:].count(4), aList[1:].count(3), aList[1:].count(2), aList[1:].count(1)]
    brList = [bList[1:].count(4), bList[1:].count(3), bList[1:].count(2), bList[1:].count(1)]
    for i in range(4):
        if arList[i] > brList[i]:
            print('A')
            break
        elif arList[i] < brList[i]:
            print('B')
            break
    else:
        if sum(arList) > sum(brList):
            print('A')
        elif sum(arList) < sum(brList):
            print('B')
        else:
            print('D')


# sol2 : 정렬
for i in range(round):
    aList = list(map(int, input().strip().split()))
    bList = list(map(int, input().strip().split()))
    soraList= sorted(aList[1:], reverse = True)
    sorbList= sorted(bList[1:], reverse = True)
    for j in range(min(len(soraList),len(sorbList))):
        if soraList[j] > sorbList[j]:
            print('A')
            break
        elif soraList[j] < sorbList[j]:
            print('B')
            break
    else:
        if len(aList) == len(bList):
            print('D')
        else:
            if len(aList) > len(bList):
                print('A')
            else:
                print('B')