import sys; input = sys.stdin.readline
# from collections import defaultdict

if __name__ == '__main__':
    king, stone, mv = map(int, input().strip().split())
    # dic = defaultdict[int]
    moveDic = {'R':0, 'L':1, 'B':2, 'T':3, 'RT':4, 'LT':5, 'RB':6, 'LB':7}
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    move = []
    for i in range(mv):
        move.append(moveDic[input()])
    for j in move:
        

