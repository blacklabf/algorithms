# SWEA 1984 : 중간 평균값 구하기
# list 요소 제거 / sum은 시간초과 될 가능성이 높으니까 대체 / sort()sorted()
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    aList = list(map(int,input().strip().split()))
    aList.sort()
    del aList[0]
    del aList[-1]
    # ans = sum(aList) // 8 반올림을 안 해서 틀림 (//와 round의 차이)
    ans = round(sum(aList) / 8)
    print('#{} {}'.format(i,ans))
