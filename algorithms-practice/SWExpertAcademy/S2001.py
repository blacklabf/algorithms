# 삼성 2001 : 파리퇴치 
import sys; input = sys.stdin.readline
t = int(input())
def main():
    for i in range(t):
        n, m = map(int, input().strip().split())
        arr = [[] * n for _ in range(n)]
        for a in range(n):
            arr[a] = list(map(int, input().strip().split()))
        ans = []
        for i in range(n-m+1):
            for j in range(n-m+1):
                sub_arr = [row[j:j+m] for row in arr[i:i+m]]
                print(arr[i:i+m], sub_arr)
                ans.append(sum(sub_arr))
        print(ans, arr)

if __name__ == '__main__':
    main()