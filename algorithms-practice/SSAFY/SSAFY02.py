import sys; input = sys.stdin.readline

if __name__ == '__main__':
    basket, tgt = map(int, input().strip().split())
    apples = [0] + list(map(int, input().strip().split()))
    idx = []

    # 벌레 알고리즘 / 죽는지 알기만 하면 됨
    # 사과있는 list에서 그것만 빼면 됨


    for i in range(len(apples) + 1):
        if apples[i] == 1:
            idx.append(i)

    for id in idx:
        for k in range(id-1, 0, -1):
            if apples[k] == 1:
                left = id - k
                break
        for r in range(id+1, basket+1, 1):
            if apples[r] == 1:
                right = r - id
                break
        if left == right:
            idx.remove(id)

    mv = 1
    lt = tgt - mv
    rt = tgt + mv

    # tgt 에서
    for z in range(tgt-1, 0, -1):
        if apples[z] == 1:
            tmpL = tgt - z
            break
    for y in range(tgt+1, basket+1, 1):
        if apples[y] == 1:
            tmpR = y - tgt
            break

    tgtList = []

    if tmpL != tmpR:
        print(0)
    else:
        for ix in idx:
            tgtList.append(tgt-ix)

    tgtList.sort()

    for t in tgtList:
        for a in range(t-1, 0, )




