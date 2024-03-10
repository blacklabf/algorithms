import sys ; input = sys.stdin.readline
n = int(input())
A = []
for i in range(n):
    a, b = map(int, input().strip().split())
    A.append([a, b])

final = sorted(A, key = lambda x : (x[1], x[0]))

for x, y in final:
    print(x, y)