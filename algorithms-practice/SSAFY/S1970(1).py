if __name__ == '__main__':
    test = int(input())
    remain = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for tc in range(1, test+1):
        money = int(input())
        ans = []
        for i in range(8):
            ans.append(money//remain[i])
            money = money % remain[i]
        print('#{}'.format(tc))
        print(*ans)
