if __name__ == '__main__':
    baguni = int(input())
    apple = int(input())
    bug = int(input()) - 1
    apples = list(input().split())
    find_index = [i for i in range(baguni) if apples[i] == '1']
    l, r = find_index[0], find_index[-1]
    if l <= bug <= r: print((bug - l) * 2 + r - bug)
    if bug < l: print(r - bug)
    if r < bug: print(bug - l)



#     n = int(input()) # 바구니의 갯수
#     # arr = [0] * (n+1)
#     apple = int(input()) # 사과의 갯수 , 안쓸거임
#     bug = int(input()) # 벌레의 위치
#     arr = [0] + list(map(int, input().split()))
#     a, b = 0, 0
#     for i in range(1, n+1):
#         if arr[i] == 1:
#             a = bug - i
#             break
#
#     for j in range(n, 0 ,-1):
#         if arr[j] == 1:
#             b = j - bug
#             break
#
#     tmp = min(a * 2 + b , b * 2 + a)
#     print(tmp)
# def main():
#
#     t = int(input())
#
#     for k in range(t):
#         n, s = map(int, input().split())
#
#         pointList = list(map(int, input().split()))
#         pointList.sort()
#
#         leftDiff = abs(pointList[0] - s)
#         rightDiff = abs(pointList[-1] -s)
#
#         sum = 0
#         if leftDiff <= rightDiff:
#             sum += leftDiff
#             for i in range(len(pointList)-1):
#                 sum += (pointList[i+1] - pointList[i])
#         else:
#             sum += rightDiff
#             for i in range(len(pointList)-1):
#                 sum += (pointList[i+1] - pointList[i])
#
#         print(f'#{k+1} {sum}')
#
#
#
#
# if __name__ == "__main__":
#     main()
