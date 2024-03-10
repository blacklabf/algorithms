# 백준 17219 : 비밀번호 찾기
import sys; input = sys.stdin.readline
n , m = map(int, input().strip().split())
pwDic = {}
for i in range(n):
    site, pw = map(str,input().strip().split())
    pwDic[site] = pw

for j in range(m):
    si = input().strip()
    print(pwDic[si])