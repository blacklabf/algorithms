# 백준 10807 : 개수 세기
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nList = list(map(int, input().strip().split()))
    num = int(input())

    # for문
    # cnt = 0
    # for i in range(n):
    #     if nList[i] == num:
    #         cnt += 1

    # count
    print(nList.count(num))

if __name__ == '__main__':
    main()