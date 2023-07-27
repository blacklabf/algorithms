import sys ; input = sys.stdin.readline

a, b, v = map(int, input().strip().split())
n = v // (a-b)

if a-b == 1:
    print(v-a+1)

elif n == 0:
    print(1)

elif n == 1:
    if v - a+b > a:          
        print(2)
    elif v - a+b <= a:
        print(1)

elif n > 1:
    if v - ((n-1)*(a-b)) > a:
        print(n + 2)
    elif v - ((n-1)*(a-b)) <= a:
        print(n + 1)