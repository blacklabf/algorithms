import sys
from collections import deque

# 맨 위에 있는 카드 버리고 다음 첫번째(2번째) 카드를 맨밑으로 옮김
# 버리는 카드를 순서대로 출력 마지막 남는 카드

if __name__ == '__main__':
    input = sys.stdin.readline
    queue = deque()
    num = int(input())
    nList = list(range(1, num+1))
    for n in nList:
        queue.append(n)

    while queue:
        a = queue.popleft()
        print(a, end=' ')
        queue.append(queue.popleft())
        if len(queue) == 1:
            print(queue.pop())
            break




