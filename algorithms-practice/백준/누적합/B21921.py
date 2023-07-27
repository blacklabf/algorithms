# 백준 21921 : 블로그 (누적합)
import sys ; input = sys.stdin.readline

n, x = map(int,input().strip().split())
nList = [0] + list(map(int, input().strip().split()))
preFix = [0] * (n+1)
ans = [0] * (n-x+1)

for i in range(1,n+1):
    preFix[i] = preFix[i-1] + nList[i]


for j in range(x,n):
    ans[j] = preFix[j] - preFix[j-x]

num = max(ans)

if max(nList) == 0:
    print('SAD')
else : 
    print(num, ans.count(num), sep = '\n')