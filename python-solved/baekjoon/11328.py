# 백준 11328 : Strfry
import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for i in range(tc):
        str1, str2 = map(str, input().strip().split())
        str3 = sorted(str1)
        str4 = sorted(str2)
        print('Possibe' if str3 == str4 else "Impossible")


        # # 아래 코드를 위에 코드 1줄로 할 수  있음
        for j in range(len(str1)):
            if str3[j] != str4[j]:
                print("Impossible")
                break
        print("Possible")
        # 위에서 else 없이 else 자리에 print문 실행하면 어떻게 되는지

        flag = False
        for j in range(len(str1)):
            if str3[j] != str4[j]:
                flag = True
                break

        if flag:
            print()
        else:

        print("Possible")
        # 위에서 else 없이 else 자리에 print문 실행하면 어떻게 되는지


if __name__ == '__main__':
    main()