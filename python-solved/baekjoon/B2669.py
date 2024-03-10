# 백준 2669 : 직사각형 네개의 합집합의 면적 구하기
import sys; input = sys.stdin.readline
squares= [list(map(int, input().strip().split())) for _ in range(4)]
tmp = 0

for a in squares:
    tmp = max(tmp, max(a))

arr = [[0]*tmp for _ in range(tmp)]

for b in squares:
    for i in range(b[0], b[2]):
        for j in range(b[1], b[3]):
            arr[i][j] = 1

answer = 0
for c in arr:
    answer += sum(c)

print(answer)






