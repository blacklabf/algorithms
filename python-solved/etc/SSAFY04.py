import sys; input = sys.stdin.readline
# 여기서 만약 idx까지 고려해줘야 한다면 dic을 어떻게 정렬할 수 있을지
# 여기서도 히든 케이스!! : 처음부터 높을 수도 있다는 걸 알아줘야 함!!
# 풀이 1
if __name__ == '__main__':
    n = int(input())
    nList = list(map(int, input().strip().split()))
    nDic = {}
    sum1 = sum(nList)
    cnt = 0
    for i in range(n):
        if nList[i] <= 0 :
            nDic[i] = i - nList[i]
        else:
            nDic[i] = i
    sDic = sorted(nDic.items(), key=lambda x:(-x[1], x[0])) # value에 대한 내림차순 / key(idx)에 대한 오름차순
    idx = 0
    while sum1 < 2*n:
        cnt += 1
        sum1 += sDic[idx][1]
        idx+=1
    print(cnt)

# 풀이 2
n = int(input())
a = list(map(int, input().split()))
S = sum(a)
tgt = 2 * n

if S >= tgt:
    print(0)
    exit()

d = [0 for _ in range(n)]
for i in range(n):
    if a[i] > 0:
        v= a[i] + i
    else:
        v = i
    # a[i] -> v
    d[i] = v - a[i] # 변화값

l = tgt - s
d.sort(reverse=True)
delta_sum = 0
for i in range(n):
    delta_sum += d[i]
    if delta_sum >= l:
        print(i+1)
        break

# 예제 입력
# 4
# -1 1 -2 3
# 출력 : 2