# 백준 1919 : 애너그램 만들기
import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    str1 = input().strip()
    str2 = input().strip()

    str1Dict = {}
    str2Dict = {}

    for x in str1:
        if x in str1Dict:
            str1Dict[x] += 1
        else:
            str1Dict[x] = 1

    for x in str2:
        if x in str2Dict :
            str2Dict[x] += 1
        else:
            str2Dict[x] = 1

    # for x in str1Dict.keys():
    #     if x in str2Dict.keys():
    #         str1Dict[x] -= str2Dict[x]

    for x in str2Dict.keys():
        if x in str1Dict.keys():
            str2Dict[x] -= str1Dict[x]

    for i in str1Dict:
        print(str1Dict[i])

    for i in str2Dict:
        print(str2Dict[i])

    # num = min(len(str1))
    # str3 = [x for x in str1 if x not in str2]
    # str4 = [y for y in str2 if y not in str1]
    # print(str3)
    # print(str4)
    # ans = len(str3) + len(str4)
    # print(ans)


if __name__ == '__main__':
    main()