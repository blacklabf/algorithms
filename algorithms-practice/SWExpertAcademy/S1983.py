# SWEA 1983 : 조교의 성적 매기기
import sys; input = sys.stdin.readline
import math
t = int(input())
dic = {1:'A+' , 2:'A0', 3:'A-' , 4:'B+', 5:'B0', 6:'B-', 7:'C+', 8:'C0', 9:'C-', 10:'D0'}
for i in range(1,t+1):
    n , k = map(int,input().strip().split())
    score = [101]
    for j in range(n):
        mid, fin, ass = map(int,input().strip().split())
        score.append(mid*0.35 + fin*0.45 + ass*0.2)
    sList = sorted(score,reverse=True)
    a = score[k]
    b = n//10
    rank = sList.index(a)
    ans = dic[math.ceil(rank/b)] # 올림을 해야 함/ 나눠 떨어지지 않으면 다음 index
    print('#{} {}'.format(i,ans))

# t = int(input())
# dic = {1:'A+' , 2:'A0', 3:'A-' , 4:'B+', 5:'B0', 6:'B-', 7:'C+', 8:'C0', 9:'C-', 10:'D0'}
# for i in range(1,t+1):
#     n , k = map(int,input().strip().split())
#     score = [101] # 100으로 하면 안됨(중복가능성)
#     for j in range(n):
#         mid, fin, ass = map(int,input().strip().split())
#         score.append(mid*0.35 + fin*0.45 + ass*0.2)
#     sList = sorted(score,reverse=True) 
#     a = score[k]
#     b = n//10
#     rank = sList.index(a)
#     print(score)
#     print(sList)
#     print(a, b,rank/b , math.ceil(rank/b))
#     ans = dic[math.ceil(rank/b)]
#     print('#{} {}'.format(i,ans))
