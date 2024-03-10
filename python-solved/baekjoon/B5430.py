# 백준 AC -> 맨 앞에서 문자 삭제를 읽고 queue를 생각함

import sys ; input = sys.stdin.readline
from collections import deque
# queue = deque() -> 원래방법대로 하면 중첩리스트로 저장됨.

t = int(input())
for i in range(t):
    tList = input().strip()
    n = int(input())
    queue = deque(input().strip()[1:-1].split(','))
    # queue.append(input().strip()[1:-1].split(','))
    for j in tList:
        if len(queue) == 0:
            print('error')
            break
        else:
            if j == 'R':
               print('[',','.join(queue),']', sep='')
            elif j == 'D':
                queue.popleft
    else:
        print('[',','queue),']', sep='')






