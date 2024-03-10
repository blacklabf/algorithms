if __name__ == '__main__':
    test = int(input())
    for tc in range(1, test+1):
        # n : 배열크기 / m : 분사수
        n, m = map(int, input().strip().split())
        arr = [list(map(int, input().strip().split())) for _ in range(n)]
        # 위, 아래, 오, 왼, 왼위, 오위 ,왼아, 오아
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, 1, -1, -1, 1, -1, 1]
        x, y = 0, 0
        tmp1, tmp2 = 0, 0
        ans = 0

        for x in range(n):
            for y in range(n):
                tmp1, tmp2 = arr[x][y], arr[x][y]
                for i in range(1, m+1):
                    for j in range(4):
                        if 0 <= x + (i * dx[j]) < n and 0 <= y + (i * dy[j]) < n:
                            tmpX = x + (i * dx[j])
                            tmpY = y + (i * dy[j])
                            tmp1 += arr[tmpX][tmpY]
                        else: continue
                    for k in range(4, 8):
                        if 0 <= x + (i * dx[k]) < n and 0 <= y + (i * dy[k]) < n:
                            tmpX = x + (i * dx[k])
                            tmpY = y + (i * dy[k])
                            tmp2 += arr[tmpX][tmpY]
                        else: continue
                ans = max(ans, tmp1, tmp2)

        print('#{} {}'.format(tc, ans))




