N = str(input())
M = int(input())
if M != 0:
    arr = list(map(int, input().split()))
else:
    arr = []


numbers = []
for i in range(10):
    if i not in arr:
        numbers.append(i)

# 100번에서 시작했을 때 얼마나 걸리는지
from_h = abs(int(N) - 100)

min_sub = 500000
num = ''
i = 0
new_num = 100
# numbers로 만들 수 있는 숫자를 모두 만들어 가장 N과 차가 작은 것 찾기
def makenum(i, num):
    global min_sub
    global new_num
    if i == len(N) + 1:
        if min_sub >= abs(int(N) - int(num)):
            min_sub = abs(int(N) - int(num))
            new_num = int(num)
        if len(num) > 1 and min_sub >= abs(int(N) - int(num[:-1])):
            min_sub = abs(int(N) - int(num[:-1]))
            new_num = int(num[:-1])
        if len(num) > 2 and min_sub >= abs(int(N) - int(num[:-2])):
            min_sub = abs(int(N) - int(num[:-2]))
            new_num = int(num[:-2])
        return
    for j in range(10 - M):
        makenum(i + 1, num + str(numbers[j]))

makenum(i, num)
# 최소 버튼 누르는 횟수는
push_num = abs(new_num - int(N)) + len(str(new_num))

# 둘 중 최솟값
print(min(from_h, push_num))