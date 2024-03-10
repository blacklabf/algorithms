# 백준 10157 : 자리배정
import sys; input = sys.stdin.readline

if __name__ == '__main__':
    c, r = map(int, input().strip().split())
    arr = [[0] * (c+1) for _ in range(r+1)]
    # 상, 우, 하 , 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    move = 0
    x, y = c, 1

    for i in range(1, r*c+1):
        if 0 < x <= c and 0 < y <= c and arr[x][y] == 0:
            arr[x][y] = i
            x += dx[move]
            y += dy[move]
        else:
            x -= dx[move]
            y -= dy[move]
            move = (move+1) % 4
            x += dx[move]
            y += dy[move]
            arr[x][y] = i
            x += dx[move]
            y += dy[move]


    target = int(input())
    flag = False

    if 1 <= target <= r*c:
        for a in range(1, c+1):
            for b in range(1, r+1):
                if arr[a][b] == target:
                    print(b, c-a)
                    flag = True
                    break
            if flag:
                break
    else: print('0')
