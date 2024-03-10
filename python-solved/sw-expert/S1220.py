# SWEA 1220 : Magnetic
import sys ; input = sys.stdin.readline

for tc in range(1, 11):
    n = int(input()) # 정사각형 한 변의 길이 : 100
    arr = [list(map(int, input().strip().split())) for _ in range(100)]
    # 테이블 위 : N / 아래 : S / 1 : N / 2: S
    new_arr = list(map(list, zip(*arr[::-1])))
    for i in range(100):
        for j in range(100):
            if new_arr[i][j] == 0 : continue
            elif new_arr[i][j] == 1:
                k = 1
                cnt = 0
                while j+ k <= 100:
                    if new_arr[i][j+k] == 2:
                        cnt +=1
