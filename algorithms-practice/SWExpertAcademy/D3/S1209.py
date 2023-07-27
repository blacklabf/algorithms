# SWEA 1209 : Sum
import sys ; input = sys.stdin.readline

for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input().strip().split())) for _ in range(100)]

    answer = 0
    row, column, lCross, rCross = 0, 0, 0, 0
    aRow, aColumn = 0, 0

    for n in range(100):
        for m in range(100):
            aRow += graph[n][m]
            aColumn += graph[m][n]
        row = max(aRow, row)
        column = max(aColumn, column)
        aRow , aColumn = 0, 0

    for c in range(100):
        lCross += graph[c][c]
        rCross += graph[c][99-c]

    answer = max(row, column, lCross, rCross)

    print('#{} {}'.format(tc, answer))