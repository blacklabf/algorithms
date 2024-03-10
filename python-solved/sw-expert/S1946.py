# # SWEA 1946 : 간단한 압축 풀기
# import sys; input = sys.stdin.readline
# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     ans = []
#     for j in range(n):
#         a , b = input().strip().split()
#         ans = ans+list(a*int(b))
#     x = len(ans) // 10
#     print('#{}'.format(i))

#     k = 1
#     while 10 * k < len(ans):
#         print(*ans[10*(k-1):(10*k)-1])
#         k += 1
#     print(*ans[10*(k-1):])
a = 'A'*10
print(type(a))
print('A'*10)