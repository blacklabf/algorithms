# SWEA 1989 : 초심자의 회문 검사
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    pal = input().strip()
    if pal == pal[::-1]:
        print('#{} {}'.format(i,1))
    else:
        print('#{} {}'.format(i,0))