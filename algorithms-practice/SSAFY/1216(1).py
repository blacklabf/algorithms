if __name__ == '__main__':
    def check(graph):
        length = 0
        flag = False
        for i in range(100):
            j, k = 0, 1
            while 0 <= j <= 99 and 0 <= j + k <= 100:
                if arr[i][j:j + k] == arr[i][j:j + k][::-1]:
                    if k == 100:
                        length = k
                        flag = True
                        break
                    else:
                        length = max(length, k)
                        print('#{} #{} #{} #{} #{}'.format(i, j , k, length, arr[i][j:j + k]))
                        k += 1
                else:
                    if j + k == 100:
                        j += 1
                        k = length
                    elif j + k < 100:
                        k += 1
            if flag: break
        return length

    for _ in range(10):
        tc = int(input())
        arr = [input().strip() for _ in range(100)]
        newArr = []
        for each in zip(*arr):
            newArr.append(each)
        ans = max(check(arr), check(newArr))


        print('#{} {}'.format(tc, ans))

