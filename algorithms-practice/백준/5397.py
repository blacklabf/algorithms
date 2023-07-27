# 백준 5397 : 키로거
from collections import deque; queue = deque()
import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    stack = []
    str = input().strip()
    for i in str:
        if i == '<':
            if len(stack) != 0:


        stack.append(i)



if __name__ == '__main__':
    main()