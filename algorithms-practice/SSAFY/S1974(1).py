if __name__ == '__main__':
    for tc in range(1, 11):
        arr = [list(map(int,input().strip().split())) for _ in range(9)]
        newArr = []
        for each in zip(*arr):
            newArr.append(each)
        cnt1 = 0
        dia = []

        for i in range(9):
            if list(set(arr[i])) == 9 and list(set(newArr[i])):
                cnt1 += 1
            else:
                print('#{} {}'.format(tc, 0))
                break

        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                dia.append(arr[r][c])
                sum += arr[r][c]

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                arr[i][j:j+3]