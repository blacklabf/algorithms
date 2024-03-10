# SWEA 1974 : 스도쿠 검증
import sys ; input = sys.stdin.readline
t = int(input())
sudoku =[[]*0 for _ in range(9)]
num = [1,2,3,4,5,6,7,8,9]
for i in range(1,t+1):
    row = 0
    column = 0
    square = []
    for j in range(9):
        sudoku[j]=list(map(int,input().strip().split()))
    for k in range(9):
        row += len(list(set(sudoku[k])))
    for k in range(0,9,3):
        for l in range(0,9,3):
            square.append(*sudoku[l][k:3])


    [[row[i] for row in sudoku[::-1]] for i in range(len(sudoku[0]))] #2차원배열회전
    # 위에 처럼 하면 sudoku 자체가 바뀌는데 sudoku는 그대로 두고 새로운 2차원 배열 하는 법
    for k in range(9):
        column += len(list(set(sudoku[k])))
    


