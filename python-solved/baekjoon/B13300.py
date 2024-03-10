# 백준 13300 : 방 배정
import sys
input = sys.stdin.readline

def main():
    students, maximum = map(int, input().strip().split())
    studentList = [[0]*2 for _ in range(7)] # index를 맞춰주기 위해 inx +1 을 해줌
    for i in range(students):
        s, grade = map(int, input().strip().split())
        studentList[grade][s] += 1

    ans = 0
    max_val = studentList[0][0]
    for i in range(7): # 7은 len(studentList)
        for j in range(2): # 2는 len(studnetList[i])
            if studentList[i][j] != 0 and studentList[i][j] % maximum == 0:
                ans += studentList[i][j] // maximum
            if studentList[i][j] != 0 and studentList[i][j] % maximum != 0:
                ans += (studentList[i][j] // maximum) + 1

    print(ans)

if __name__ == '__main__':
    main()