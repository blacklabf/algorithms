import sys; input = sys.stdin.readline

if __name__ == '__main__':
    test = int(input())
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    for tc in range(1, test+1):
        n = int(input())
        arr = [input().strip() for _ in range(n)]
        colArr = []
        for each in zip(*arr):
            colArr.append(each)

        # 가로탐색
        for i in range(n):
            cnt1 = 1
            for j in range(n-1):
                if j + 1 >= n : continue
                elif arr[i][j] == 'o' and arr[i][j+1] == 'o':
                    cnt1 += 1
                elif arr[i][j] == 'o' and arr[i][j+1] !='o':
                    cnt1 = 1

        # 세로탐색
        for k in range(n):
            cnt2 = 1
            for l in range(n-1):
                if colArr[k][l] == 'o' and colArr[k][l+1] == 'o':
                    cnt2 += 1
                elif colArr[k][l] == 'o' and colArr[k][l+1] !='o':
                    cnt2 = 1

        # 왼쪽대각선 탐색
        for q in range(n-1):
            cnt3 = 1
            if arr[q][q] == 'o' and arr[q+1][q + 1] == 'o':
                cnt3 += 1
            elif arr[q][q] == 'o' and arr[q+1][q + 1] != 'o':
                cnt3 = 1

        # 오른쪽대각선 탐색
        for r in range(n-1):
            cnt4 = 1
            if n-r >= n: continue
            elif arr[r][n -1 -r] == 'o' and arr[r+1][n -r] == 'o':
                cnt4 += 1
                #print(cnt4)
            elif arr[r][n -1 -r] == 'o' and arr[r+1][n -r] != 'o':
                cnt4 = 1
                #print(cnt4)
            else: print('##')


        if cnt1 >= 5 or cnt2 >= 5 or cnt3 >= 5 or cnt4 >= 5:
            print('#{} {}'.format(tc, 'YES'))
        else:
            print('#{} {}'.format(tc, 'NO'))
