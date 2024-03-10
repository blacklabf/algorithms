# SWEA 1288 : 새로운 불면증 치료법
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    n = int(input())
    ans = []
    j = 1
    cnt = 0
    while len(list(set(ans))) < 10:
        m = n * j
        num = [int(d) for d in str(m)]
        ans.extend(num) #2자리이상의 숫자를 한 자리씩 나눠서 넣는 방법
        j += 1
        cnt += 1
    print('#{} {}'.format(i,m))
    

