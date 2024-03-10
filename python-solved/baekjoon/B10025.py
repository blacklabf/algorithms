# 백준 10025 : 게으른 백곰 (누적합)
# 입력 - 얼음의 양 / 좌표 순서임

import sys ; input = sys.stdin.readline
aList = [0] * 1000001
preFix = [0] * 1000001
num = []
ans = []
n , k = map(int,input().strip().split())
for _ in range(n):
    a , b = map(int, input().strip().split())
    num.append(b)
    aList[b] = a


# 1. 누적합으로 하면 100000번 더해야 함 
# 1-1. -> min/max 시간초과니까 이분탐색을 한 번 더 써야 함.
# 2. n이 작을 때에는 100000번 하면 비효율적이니까 n번만 하고 싶음

# 1.
for i in range(1,n+1):
    preFix[i] = preFix[i-1] + aList[i]
for n in num:
    ans.append(preFix[n+k] - preFix[n-k])
print(max(ans))
