# 백준 2605 : 줄 세우기
import sys; input = sys.stdin.readline

def main():
    num = int(input())
    students = list(map(int, input().strip().split()))
    answer = []

    idx = num
    for i in range(num):
        idx = i - students[i]
        answer.insert(idx, i+1)

    print(*answer)

if __name__ == '__main__':
    main()