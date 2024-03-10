if __name__ == '__main__':
    test = int(input())
    for tc in range(1, test+1):
        a, b, c, d = map(int, input().strip().split())
        if a+c+1 < 12 and b + d >= 60:
            print('#{} {} {}'.format(tc, a+c+1, b+d-60))
        elif