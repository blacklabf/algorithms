# SWEA 1976 : 시각 덧셈   
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    a, b, c, d = map(int,input().strip().split())
    if b + d >= 60 and a+c > 12:
        print('#{} {} {}'.format(i,a+c+1-12,b+d-60))
    elif b + d >= 60 and a+c <= 12:
        print('#{} {} {}'.format(i,a+c+1,b+d-60))
    elif b + d < 60 and a+c <= 12:
        print('#{} {} {}'.format(i,a+c,b+d))
    else:
        print('#{} {} {}'.format(i,a+c-12,b+d))
