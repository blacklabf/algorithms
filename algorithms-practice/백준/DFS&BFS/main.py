# 얕은 복사 깊은 복사
# 얕은 복수 : 주소가 복사되는 거   -> 아래 코드
# 깊은 복사 : 데이터를 가져오는 거 -> 이중배열 : [[] * for _ in range()]
a = [0] * 3
b = [a] * 3


print(id(a))

print(id(b[0]))
print(id(b[1]))
print(id(b[2]))

graph1 = [[] for _ in range (5)] 
graph2= [[] * (5) for _ in range(5)]
print(graph1, graph2)

b[1][0] = 1
print(a)

# 언패킹 연산자 *

c = [1, 2, 3]

print(c)
print(1, 2, 3)