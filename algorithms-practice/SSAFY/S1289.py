# SWEA 1289 : 원재의 메모리 복구하기
# 000 에서 주어진 거로 바꿔지는 거
def main():
    test = int(input())
    for tc in range(1, test+1):
        memory = list(map(int, input()))
        init = [0 for _ in range(len(memory))]
        cnt = 0
        for i in range(len(memory)):
            if memory[i] != init[i]:
                while i != len(memory):
                    memory[i] ^= 1
                    i +=1
                cnt +=1
        print('#{} {}'.format(tc, cnt))

if __name__ == '__main__':
    main()