# 백준 10994: 별찍기19
import sys ; input = sys.stdin.readline
n = int(input())
ans = [[] * (4*n-1) for _ in range(4*n-1)]
for i in range(1,4*n-2):
    if i % 2 != 0 :
        ans[i] = ['*'] * (4*n-1)
    else :
        ans[i] = [' '] * (4*n-1)
for j in range(1,4*n-2):
    if j < ((4*n-3)/2) + 1 :
        k = j
        while k >= 1:
            if j % 2 != 0:
                ans[j][(k-1)] = ' '
                ans[j][(4*n-2)-(k-1)] = ' '
                k -= 2
            else : 
                ans[j][(k-1)] = '*'
                ans[j][(4*n-2)-(k-1)] = '*'
                k -= 2
        print(*ans[j][1:(4*n-2)],sep='')
    else:
        ans[j] = ans[(4*n)-2-j]
        print(*ans[j][1:(4*n-2)],sep='')


# for j in range(1,4*n-2):
#     if j < ((4*n-3)/2) + 1 :
#         if j % 2 != 0:
#             ans[j][(j-1)] = ' '
#             ans[j][(4*n-2)-(j-1)] = ' '
#             print(*ans[j][1:(4*n-2)])
#         else : 
#             ans[j][(j-1)] = '*'
#             ans[j][(4*n-2)-(j-1)] = '*' 
#             print(*ans[j][1:(4*n-2)])
#     else:
#         ans[j] = ans[(4*n)-2-j]
#         print(*ans[j][1:(4*n-2)])

        
        
