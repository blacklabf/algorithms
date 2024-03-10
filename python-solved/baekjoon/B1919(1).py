import sys; input = sys.stdin.readline
from collections import defaultdict
if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    cnt = 0

    for s in str1:
        if s not in str2:
            cnt += 1

    for k in str2:
        if k not in str1:
            cnt += 1

    print(cnt)