# 백준 1475 : 방 번호
import sys
input = sys.stdin.readline


def main():
    n = input().strip()
    nList = [0] * 10

    for num in n:
        nList[int(num)] += 1

    # while문 돌리지 말고 그냥 inx 6,9 자리의 수를 가지고 계산을 하면 될 듯
    # 아래 코드를 더 깔끔하게 정리하고 -> 했음
    total = nList[6] + nList[9]
    if total % 2 == 0:
        nList[6] = nList[9] = total // 2
    else:
        nList[6] = nList[9] = total // 2 + 1

    print(max(nList))

if __name__ == '__main__':
    main()