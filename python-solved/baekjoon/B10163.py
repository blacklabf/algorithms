# 백준 10163 : 색종이
import sys; input =sys.stdin.readline

if __name__ == '__main__':
    arr = [[0] * 1001 for _ in range(1001)]
    num = int(input())
    ans = [0] * num

    for tc in range(num):
        a, b, c, d = map(int, input().strip().split())
        # index slicing으로 가능한지
        for i in range(c):
            for j in range(d):
                if arr[a+i][b+j] == 0:
                    arr[a+i][b+j]= 1
                    ans[tc] += 1
                    if tc > 1:
                        for k in range(tc):
                            ans[tc-k] -=




