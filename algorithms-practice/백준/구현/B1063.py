# 백준 1063 : 킹 
# dictionary로 구현가능
import sys; input = sys.stdin.readline
king, stone, n = input().split()
dx = [-1, 0 , 1, 0 , -1, -1, 1, 1] # L T R B LT LB RT RB
dy = [0, 1, 0, -1 , 1, -1 ,1 ,-1]
move = ['L', 'T', 'R','B','LT', 'LB','RT','RB']
for i in range(int(n)):
    

