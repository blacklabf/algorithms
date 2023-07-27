# # SWEA 2005 : 파스칼의 삼각형

import sys; input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    print('#{}'.format(i))
    n = int(input())
    ans = [[0] * l for l in range(1,n+1)] # range(n)이 아니고 range(1,n+1)
    for j in range(n):
        ans[j][0] = 1
        ans[j][j] = 1
        for k in range(1,j):
            ans[j][k] = ans[j-1][k-1] + ans[j-1][k]
        print(*ans[j],sep=' ')

# 틀린 코드
# import sys; input = sys.stdin.readline
# t = int(input())
# for i in range(1,t+1):
#     print('#{}'.format(i))
#     n = int(input())
#     ans = [[0] * l for l in range(1,n+1)] # range(n)이 아니고 range(1,n+1)
#     ans[0][0] = 1 # ans[0] = 1 , ans[0] = [1] 차이 알기
#     for j in range(1,n):
#         ans[j][0] = 1
#         ans[j][j] = 1
#         for k in range(1,j):
#             ans[j][k] = ans[j-1][k-1] + ans[j-1][k]
#         print(*ans[j],sep=' ')


# 1차원 배열로 초기화
# import sys; input = sys.stdin.readline
# t = int(input())
# for i in range(1,t+1):
#     print('#{}'.format(i))
#     n = int(input())
#     ans = [0] * n # 1차원 배열로 초기화
#     ans[0] = [1] # 첫 번째 요소는 리스트로 변환
#     for j in range(1,n):
#         ans[j] = [0] * (j+1) # j번째 행은 j+1 크기의 리스트로 초기화
#         ans[j][0] = 1
#         ans[j][j] = 1
#         for k in range(1,j):
#             ans[j][k] = ans[j][k-1] + ans[j-1][k]
#         print(*ans[j],sep=' ')

# 2차원 배열로 초기화
# import sys; input = sys.stdin.readline
# t = int(input())
# for i in range(1,t+1):
#     print('#{}'.format(i))
#     n = int(input())
#     ans = [[0] * j for j in range(1, n+1)]
#     ans[0][0] = 1
#     for j in range(1,n):
#         ans[j][0] = 1
#         ans[j][j] = 1
#         for k in range(1,j):
#             ans[j][k] = ans[j][k-1] + ans[j-1][k]
#         print(*ans[j],sep=' ')
