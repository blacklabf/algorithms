# SWEA 1966 : 숫자를 정렬하자
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    n = int(input())
    numbers = list(map(int,input().strip().split()))
    numbers.sort()
    print('#{}'.format(i),*numbers,sep=' ')
