# 백준 2309 : 일곱 난쟁이
import sys; input = sys.stdin.readline
import itertools

height = [int(input()) for _ in range(9)]
height.sort()

for i in itertools.combinations(height, 7):
    if sum(i) == 100:
        # 출력전에 sort 해줘야 함
        # arr = list(i).sort() 도 안됨
        arr = list(i)
        arr.sort()
        print(*arr, sep='\n')
        break
