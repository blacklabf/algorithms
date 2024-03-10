# 백준 1244 : 스위치 켜고 끄기
import sys
input = sys.stdin.readline

# 남학생(1) : 배수 스위치
# 여학생(2) : 받은 수의 대칭인 거에 대해 스위치 (1. 대칭 / 2. 끝날 수 있음 / 3. 대칭 없으면 하나만 바꿈)
# 입력 : 스위치상태  / 성별과 받은 수
# 출력 : 스위치들의 마지막 상태

# idx

def main():
    sNum = int(input())
    switch = [0] + list(map(int, input().strip().split()))
    students = int(input())
    for i in range(students):
        a, b = map(int, input().strip().split())
        if a == 1:
            c = b
            while c <= sNum:
                switch[c]^= 1
                c += b
        elif a == 2:
            switch[b] ^= 1
            k = 1
            while b-k >= 1 and b+k <= sNum and switch[b-k] == switch[b+k]:
                switch[b-k] ^= 1
                switch[b+k] ^= 1
                k += 1

    if len(switch) <= 20:
        print(*switch[1:], sep=' ')
    else:
        n = 1
        print(*switch[1:21], sep=' ')
        while 20*n+1 <= len(switch):
            print(*switch[20*n+1:20*(n+1)+1], sep=' ')
            n += 1
        # python은 slicing할 때 idx를 넘어도 그냥 끝까지 출력됨


if __name__ == '__main__':
    main()