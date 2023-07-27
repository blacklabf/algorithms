# 백준 2578 : 빙고
import sys
input = sys.stdin.readline

# cnt를 체크할 때마다 초기화를 해주지 않으면 누적되어서 hello가 계속 더해짐
# 전체 다 cnt를 초기화해줘도 되고 변수명을 다 바꿔서 해줘도 될 듯
def check():
    hello= 0
    # 가로 체크
    for i in range(1, 6):
        cnt = 0
        for j in range(1, 6):
            if answer[i][j] == 1:
                cnt += 1
        if cnt == 5:
            hello += 1
    # 세로 체크
    for i in range(1, 6):
        cnt = 0
        for j in range(1, 6):
            if answer[j][i] == 1:
                cnt += 1
        if cnt == 5:
            hello += 1
    # 대각선 체크 : 대각선은 한 줄만 확인하면 되니까 for문 1개에 if 문의 위치가 for문이 끝난 후임.
    cnt = 0
    for i in range(1, 6):
        if answer[i][i] == 1:
            cnt += 1
    if cnt == 5:
        hello += 1
    # 반대 대각선
    cnt = 0
    for i in range(1, 6):
        if answer[i][6-i] == 1:
            cnt += 1
    if cnt == 5:
        hello += 1
    return hello # return hello 하면 어떻게 되지?

def check_by_chan():
    cnt = 0
    for i in range(1, 6, 1):
        if sum(answer[i]) == 5: cnt += 1
    tmp_answer = list(zip(*answer))
    for i in range(1, 6, 1):
        if sum(tmp_answer[i]) == 5: cnt += 1

    flag = True
    for x in range(1, 6, 1):
        if answer[x][x] != 1:
            flag = False
            break
    if flag: cnt+=1

    flag = True
    for i in range(1, 6, 1):
        if answer[i][6-i] !=1:
            flag = False
            break
    if flag: cnt += 1

    return cnt >= 3

bingo = [[0] * 6 for _ in range(6)]
answer = [[0] * 6 for _ in range(6)] # 방문처리로 할 예정
ans = []
for i in range(1, 6):
    bingo[i] = [0] + list(map(int, input().strip().split()))
for j in range(5):
    ans.extend(list(map(int, input().strip().split()))) # append에서 여러 개 요소 가능한지 -> extend & list 가능

for k in range(25):
    for i , v in enumerate(bingo):
        if ans[k] in v:
            j = v.index(ans[k])
            answer[i][j] = 1
            break

    if check_by_chan():
        print(k+1)
        break

print(*answer)