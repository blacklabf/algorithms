import sys; input = sys.stdin.readline

if __name__ == '__main__':
    w, h = map(int, input().strip().split())
    p, q = map(int, input().strip().split())
    time = int(input())
    # 초기좌표
    x, y = q - 1, w - p
    # 짝수 : 왼위 / 홀수 (번갈아가면서) : 오위, 왼아
    # 4 나머지로 비교하려고 하나 더 만듦
    dx = [-1, -1, 0, 1]
    dy = [-1, 1, 0, -1]
    mv = 1
    arr = [[0] * w for _ in range(h)]
    cnt = 0
    change = 1
    while cnt <= time:
        cnt += 1
        x += dx[mv]
        y += dy[mv]
        if 0 <= x < h and 0 <= y < w : continue
        else:
            x -= dx[mv]
            y -= dy[mv]
            change += 1
            if change % 2 == 0:
                mv = 0
                x += dx[mv]
                y += dy[mv]
            else:
                mv = change % 4
                x += dx[mv]
                y += dy[mv]


    print(h-y, x+1)

