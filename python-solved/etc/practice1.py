if __name__ == '__main__':
    # N*N 배열
    n = int(input())
    arr = [[0] * (n+1) for _ in range(n+1)]
    xList = []
    yList = []
    people = int(input())
    for i in range(people):
        x, y = map(int, input().split())
        xList.append(x)
        yList.append(y)
    xMax = max(xList)
    yMin = min(yList)
    yMax = max(yList)
    ans1 = xMax - 1 # 고정
    ans2 = n - yMin
    ans3 = yMax - 1
    ans = min(ans1 + ans2 , ans1 + ans3)
    print(ans)

