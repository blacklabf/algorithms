# SWEA 1284 : 수도 요금 경쟁
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    p, q, r, s ,w = map(int,input().strip().split())
    acom = p*w
    if w <= r:
        bcom = q
    else:
        bcom = q + s * (w-r)
    print('#{} {}'.format(i, min(acom,bcom)))