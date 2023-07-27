# 삼성 1204 : 최빈수 구하기
import sys ; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    num = int(input())
    dic = {}
    score = list(map(int,input().strip().split()))
    score.sort()
    # print(score)
    # print( ' ')
    for a in score: #key값이 점수
        if a not in dic:
            dic[a] = 1
        else :
            dic[a] += 1
    sDic = sorted(dic.items(), key = lambda x: (-x[1], x[0])) # value 내림차순 / key 오름차순
    # print(sDic)
    # print( ' ')

    if sDic[0][1] == sDic[1][1]:
        b = 1
        while sDic[0][1] == sDic[b][1]:
            b +=1
        else :
            print('#{} {}'.format(i,sDic[b-1][0]))
    else :
        print('#{} {}'.format(i,sDic[0][0])) #key값이 출력
