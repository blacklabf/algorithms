import sys; input = sys.stdin.readline

if __name__ == '__main__':

    test = int(input())
    for tc in range(1, test+1):
        n = int(input()) # 참조만하면 global 선언을 안 해도 된다고 했던 거 같음
        arr = [input().strip() for _ in range(n)]
        dx = [0, 1, 1, 1]
        dy = [1, 0, 1, -1]
        cnt = 0
        flag = True

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'o':
                    for mv in range(4):
                        x, y = i, j
                        cnt = 0
                        # while문을 통해 연속을 확인할 수 있음
                        while 0 <= x <= n - 1 and 0 <= y <= n - 1 and arr[x][y] == 'o':
                            cnt += 1
                            x += dx[mv]
                            y += dy[mv]
                            if cnt == 5:
                                flag = False
                                print('#{} {}'.format(tc, 'YES'))
                                break

        if flag :
            print('#{} {}'.format(tc,'NO'))






