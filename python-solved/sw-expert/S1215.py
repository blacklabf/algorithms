# SWEA 1215 : 회문1
import sys
input = sys.stdin.readline

def main():
    for t in range(10):
        target = int(input())
        board = [input().strip() for _ in range(8)]
        cnt = 0

        for i in range(8):
            for j in range(8 - target + 1):
                str1 = board[i][j:j+target]
                if str1 == str1[::-1]:
                    cnt += 1

                str2 = [board[j + k][i] for k in range(target)]
                if str2 == str2[::-1]:
                    cnt += 1
        print('#{} {}'.format(t, cnt))




if __name__ == '__main__':
    main()
