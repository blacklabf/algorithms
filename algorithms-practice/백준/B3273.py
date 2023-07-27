# 백준 3273 : 두 수의 합
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    # arr = list(map(int, input().strip().split()))
    # arr.sort()
    arr = sorted(map(int, input().split()))
    x = int(input())
    left, right = 0, n-1
    ans = 0

    while left < right:
        tmp = arr[left] + arr[right]
        if tmp == x:
            ans += 1
            left += 1
            right -= 1
        elif tmp > x:
            right -= 1
        elif tmp < x:
            left += 1

    print(ans)

if __name__ == '__main__':
    main()