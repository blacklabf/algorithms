import sys; input = sys.stdin.readline
if __name__ == '__main__':
    n , m = map(int, input().strip().split())
    wait = int(input())
    arr = [[0] * n for _ in range(m)]
    x, y = m-1, 0
    # 상, 우, 하, 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    move = 0
    for num in range(1, (n*m)+1):
        arr[x][y] = num
        x += dx[move]
        y += dy[move]
        if 0 <= x < m and 0 <= y < n and arr[x][y] == 0: continue
        else:
            x -= dx[move]
            y -= dy[move]
            move = (move+1) %  4
            x += dx[move]
            y += dy[move]

    flag = True

    for i in range(m):
        for j in range(n):
            if arr[i][j] == wait:
                flag = False
                print(j+1, m-i)
                break
    if flag:
        print('0')


