# 백준 2578 : 빙고
import sys
input = sys.stdin.readline

# 함수 만들어서 해보기! 재귀로 !


def main():
    bingo = [list(map(int, input().strip().split())) for _ in range(5)]
    ans = [list(map(int, input().strip().split())) for _ in range(5)]

    for i in range(5):
        for j in range(5):
            ans[i][j]
if __name__ == '__main__':
    main()