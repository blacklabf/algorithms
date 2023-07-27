# 백준 11003 : 최솟값 찾기
import sys
input = sys.stdin.readline

def main():
    n , l = map(int,input().strip().split())
    aList = list(map(int, input().strip().split()))

    for i in range(n):
        if i-l+1 >=0 : # 문제에서는 idx가 1부터지만 나는 0부터
            print(min(aList[i-l+1 : i]), end=' ')
    # D1 : A(1-3+1) ~ A1 까지중 최솟값
    # D2 : A(2-3+1) ~ A2 까지 중 최솟값
    # D3 : A(3-3+1) ~ A3 까지 중 최솟값
    # D4 : A(4-3+1) ~ A4 까지 중 최솟값



if __name__ == '__main__':
    main()