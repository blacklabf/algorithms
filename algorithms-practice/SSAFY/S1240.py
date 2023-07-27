# SWEA 1240 : 단순 2진 암호코드

# 문자열을 뒤집어서 int형으로 바꿔주면 앞에 0이 다 지워지기 때문에 거기서부터 56자리까지를 하나의 list로 받으면 됨
# 처음 1이 나오는 구간을 찾는 것보다 나음

import sys ; input = sys.stdin.readline

if __name__ == '__main__':

    test = int(input())
    for tc in range(1, test+1):
        n, m = map(int, input().strip().split())
        arr = [list(map(int, input().strip())) for _ in range(n)] # int를  list로 함
        code = []
        code1 = []
        flag = False
        for i in range(n):
            if arr[i].count(0) == m : continue
            else:
                for j in range(m):
                    arr1 = arr[i][::-1]
                    if arr1[j] != 0:
                        code = arr1[j: j+56][::-1]
                        code1 = list(map(str, code))
                        flag = True
                        break
                if flag:
                    break

        dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }

        aList = []
        for k in range(0, 50, 7): # 49까지 선택
            str1 = ''.join(code1[k:k+7])
            aList.append(dic[str1])

        oddSum = 0
        evenSum = 0
        ans = 0

        for l in range(0,7,2):
            oddSum += aList[l]
            evenSum += aList[l+1]


        ans = str(oddSum * 3 + evenSum)

        if ans[-1] == '0' : # type 조심하기! 그냥 0 아니고 문자열 0!!!
            print('#{} {}'.format(tc, sum(aList)))
        else:
            print('#{} {}'.format(tc, 0))


