# 백준 14696 : 딱지놀이
import sys
input = sys.stdin.readline

# 별, 동그라미, 네모, 세모 순으로 쎔 (4,3,2,1)
if __name__ == '__main__':
    round = int(input())
    Anum, Apattern  = map(int, input().strip().split())
    Bnum, Bpattern = map(int, input().strip().split())

