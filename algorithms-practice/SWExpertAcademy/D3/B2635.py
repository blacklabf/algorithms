# 백준 2635 : 수 이어가기
import sys ; input = sys.stdin.readline

if __name__ == '__main__':
    num = int(input())
    length = 0
    a = 0
    ans = []

    while a >= 0:
        for i in range(1, num+1):
            a = i
            flag = False
            numList = [num]
            while a >= 0:
                numList.append(a)
                a = numList[len(numList) -2] - numList[len(numList) -1]

            aLength = max(length, len(numList))
            if aLength > length:
                length = aLength
                flag = True
                if length :
                    ans = numList

    print(length)
    print(*ans)