# SWEA 2805 : 농작물 수확하기
import sys
input = sys.stdin.readline

test = int(input())
for tc in range(1, test+1):
    n = int(input())
    nList = [list(map(int, str(input().strip()))) for _ in range(n)]
    answer = 0
    x, y = n//2, n//2
    k, l = n//2 , n//2 +1
    answer -= sum(nList[x][y-k:y+l])

    for j in range(n//2 +1):
        answer += sum(nList[x-j][y-k:y+l])
        answer += sum(nList[x+j][y-k:y+l])
        k -= 1
        l -= 1

    print('#{} {}'.format(tc, answer))

