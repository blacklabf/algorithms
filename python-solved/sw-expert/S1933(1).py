if __name__ == '__main__':
    n = int(input())
    nList = []
    for i in range(1, n+1):
        if n % i == 0:
            nList.append(i)
    ans = list(set(nList))
    print(*ans)