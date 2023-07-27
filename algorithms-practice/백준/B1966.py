# 백준 프린터큐
# 문서의 개수 , 궁금한 문서(0부터 시작)
# 중요도 
from collections import deque
import sys ; input = sys.stdin.readline
queue = deque()
order = 0
idx = []

t = int(input())
for i in range(t):
    n , q = map(int,input().strip().split())
    aList = list(map(int, input().strip().split()))
    if 
