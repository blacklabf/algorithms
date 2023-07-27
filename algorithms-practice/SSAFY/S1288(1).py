if __name__ == '__main__':
    # solve0. 이전 풀이
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        ans = []
        j = 1
        cnt = 0
        while len(list(set(ans))) < 10:
            m = n * j
            num = [int(d) for d in str(m)]
            ans.extend(num)
            j += 1
            cnt += 1
       print('#{} {}'.format(i, m))

    # solve1. set이용
    test = int(input())
    for tc in range(1, test+1):
        num = int(input())
        nList = list(map(int, str(num)))
        n = 1
        num1 = 1
        while True:
            if len(list(set(nList))) == 10:
                print('#{} {}'.format(tc, num1))
                break
            else:
                n += 1
                num1 = num * n
                for i in list(map(int, str(num1))):
                    nList.append(i)




