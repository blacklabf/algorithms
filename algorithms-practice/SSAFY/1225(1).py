from collections import deque
queue = deque()

if __name__ == '__main__':
    for _ in range(10):
        tc = int(input())
        code = list(map(int, input().strip().split()))

        for num in code:
            queue.append(num)
        i = 1

        while list(queue)[-1] > 0:
            fst = queue.popleft()
            fst -= i
            if fst <=0 :
                queue.append(0)
                break
            else:
                queue.append(fst)
            i = (i + 1) % 6
            if i == 0:
                i += 1
        print('#{}'.format(tc), *queue)
        while queue:
            queue.popleft()

