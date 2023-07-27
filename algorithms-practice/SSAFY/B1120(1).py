if __name__ == '__main__':
    # A의 길이가 B의 길이보다 작거나 같다
    # A의 길이가 B의 길이와 같아질 때 까지 1) A 앞에 추가 2) A 뒤에 추가 => 차이 최소
    aList, bList = input().strip().split()
    for i in range(len(aList)):
        
