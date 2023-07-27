# SWEA 1225 : 암호생성기
# 문제 잘 읽기!! 5까지만 감소

# so1. queue 사용 -> 답 안나옴
from collections import deque

queue = deque()

if __name__ == '__main__':
       for _ in range(10):
        tc = int(input())
        numList = list(map(int, input().strip().split()))
        for i in range(8):
            queue.append(numList[i])

        a = queue.popleft()
        k = 1
        while a-k >= 0:
            queue.append(a-k)
            a = queue.popleft()
            k = (k+1) % 6
            if k == 0:
                k+=1

        queue.append(0)
        print('#{}'.format(tc), *queue)

# so1 2. list 인덱스로
if __name__ == '__main__':
    for _ in range(10):
        tc = int(input())
        numList = list(map(int, input().strip().split()))

        k = 1
        while numList[0] - k >= 0:
            numList[7] = numList[0] - k
            for j in range(7):
                numList[j] = numList[j + 1]
            k = (k + 1) % 6
            if k == 0:
                k += 1

        numList[7] = 0

        print('#{}'.format(tc), *numList)