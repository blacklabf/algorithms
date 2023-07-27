# 싸피 01 : 같은 점에 모이기 (구현) - 오후 2시 10분

# 가운데를 기점으로 많은 쪽 대각선 방향으로 움직이기
# 간단하게 생각하기 - 너무 많은 경우의 수를 생각하면 무조건 틀림
# xList의 평균이 가운데보다 크면 오른쪽
# yList의 평균이 가운데보다 크면 아래쪽 -> 근데 위로밖에 못 올라가니까 양쪽 위아래 만 생각
if __name__ == '__main__':
    n = int(input())
    # arr = [0 * (n+1) for _ in range(n+1)]
    xList = []
    yList = []
    p = int(input())
    ans = 0
    cnt1 = 0
    cnt2 = 0

    for i in range(p):
        x, y = map(int, input().strip().split())
        xList.append(x)
        yList.append(y)
    ans += max(xList) -1
    cnt1 = max(yList) -1
    cnt2 = 20 - min(yList)
    ans += min(cnt1, cnt2)

    print('#{}'.format(ans))






