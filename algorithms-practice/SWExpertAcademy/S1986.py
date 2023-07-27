# SWEA 1986 : 지그재그 숫자
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    n = int(input())
    even = [i for i in range(1,n+1) if i%2 == 0] # 이 표현 진짜 좋음!
    odd = [j for j in range(1,n+1) if j%2 ==1]
    ans = sum(odd) - sum(even)
    print('#{} {}'.format(i,ans))