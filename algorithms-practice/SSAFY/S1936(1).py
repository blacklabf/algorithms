if __name__  == '__main__':
    a, b = map(int, input().strip().split())
    if a == 1 and b == 2:
        print('B')
    elif a == 2 and b == 3:
        print('B')
    elif a == 3 and b == 1:
        print('B')
    else:
        print('A')


    # Dict를 이용한 풀이
    a, b = map(int, input().strip().split())
    bDic = {1:2, 2:3, 3:1}
    if bDic[a] == b:
        print('B')
    else:
        print('A')