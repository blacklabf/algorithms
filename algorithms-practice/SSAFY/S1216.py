# SWEA 1216 : 회문2
import sys ; input = sys.stdin.readline

if __name__ == '__main__':
    # for _ in range(10):
    tc = int(input())
    arr = [input().strip() for _ in range(100)]
    arrList = list(map(list, zip(*arr[::-1])))

    k = 1
    for i in range(100):
        j = 0
        while j+k <=100:
            if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                k += 1
            else:
                j +=1

    # # 특정 열 추출하고 싶은데 아예 틀림
    # c = 1
    # for a in range(100):
    #     b = 0
    #     while b + c <= 100:
    #         if arr[b:b+c][a] == arr[b:b+c][a][::-1]:
    #             c += 1
    #         else:
    #             b += 1

    # # zip 이용 : 2번째 tc 틀림
    # c = 1
    # for a in range(100):
    #     b = 0
    #     while b+c <=100:
    #         if arrList[a][b:b+c] == arrList[a][b:b+c][::-1]:
    #             c += 1
    #             print(a, b, c)
    #         else:
    #             b +=1

    print('#{} {} {}'.format(tc, k, c))