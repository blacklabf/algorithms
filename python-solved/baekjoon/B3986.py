# 백준 3986 : 좋은 단어
# cnt랑 stack의 위치를 바꿔서 초기화 함
# if - elif - else 각각 print(* / & / @) 이렇게 해서 각각 디버깅해서 확인함.
# 2 ; ABABBABA ; ABBBABAABABA 에 대한 반례 생각

import sys; input = sys.stdin.readline
n = int(input())
cnt = 0 # cnt는 여기서 초기화
for i in range(n):
    stack = [] # stack을 여기서 초기화 해야 함!
    aList = input().strip()
    for j in aList:
        if j not in stack or j != stack[-1]: # or 뒷부분을 안하면 추가반례통과못함
            stack.append(j)
        elif j == stack[-1]:
            stack.pop()
        else:
            break
    if len(stack) == 0:
        cnt += 1
print(cnt)

