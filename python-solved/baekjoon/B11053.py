import sys ; input = sys.stdin.readline
n = int(input())
a = list(map(int,input().strip().split()))

d = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if a[i] >= a[j]:
            d[i+1] = max(d[i]+1, d[j])
print(d[n])