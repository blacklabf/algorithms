import sys; input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(10):
        tc = int(input())
        target = input().strip()
        str1 = input().strip()
        ans = 0
        for i in range(len(str1) - len(target) + 1):
            if str1[i:i+len(target)] == target:
                ans += 1
        print('#{} {}'.format(tc, ans))