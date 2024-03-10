# 백준 2628 : 종이자르기
import sys; input = sys.stdin.readline

if __name__ == '__main__':
    column , row = map(int, input().strip().split())
    num = int(input())
    rowList = [0, row]
    columnList = [0, column]
    rowDiff, columnDiff = 0, 0

    for i in range(num):
        a , b= map(int,input().strip().split())
        if a == 0:
            rowList.append(b)
        else:
            columnList.append(b)

    rowList.sort()
    columnList.sort()

    for j in range(len(rowList)-1):
        rowDiff = max(rowDiff, rowList[j+1]-rowList[j])

    for k in range(len(columnList)-1):
        columnDiff = max(columnDiff, columnList[k+1]-columnList[k])

    print(rowDiff * columnDiff)

