import sys; input = sys.stdin.readline
from collections import defaultdict

if __name__ == '__main__':

    test = int(input())
    for _ in range(test):
        tc = int(input())
        score = list(map(int, input().strip().split()))
        score.sort(reverse=True) # 내림차순으로 정렬
        scoreDic = defaultdict(int)
        for i in score: scoreDic[i] +=1
        sValue = scoreDic.values()
        ans = max(sValue)
        for key, value in scoreDic.items():
            if value == ans:
                print('#{} {}'.format(tc, key))
                break