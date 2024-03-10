# 백준 설탕배달 2839
# Top - bottom 으로 해서 3 뺸거랑 5뺸거 중에 비교
import sys ; input = sys.stdin.readline
n = int(input())

d = [0] * 5001

d[3] = 1
d[4] = -1
d[5] = 1

for i in range(5002):
    d[i] = ma



m = n % 5
if m % 3 != 0 and n % 3 != 0:
    print(-1)
elif m % 3 == 0:
    a = n // 5
    b = m // 3
    print(a+b)
elif n % 3 == 0 and m % 3 != 0:
    print(n//3)
