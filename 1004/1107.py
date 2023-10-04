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

# N의 길이를 가지는 리스트를 만들고 첫 자리부터 비교하면서 차가 작은 것 찾기
num = [0] * len(N)
# 처음의 num자리는 만약 numbers에 N의 첫 자리가 있다면 그것
if N[0] in numbers:
    num[0] = N[0]
# 아니면 차가 작은 것 찾기
else:
    min_sub = 10
    for i in numbers:
        if min_sub > abs(i - int(N[0])):
            min_sub = abs(i - int(N[0]))
            num[0] = i

# # 이제 num을 돌면서 차가 작은 것을 찾기
# for i in range(1, len(N)):
#     # i 바로 전이 N에 있는 숫자와 같으면 차가 가장 작은 것을 찾으면 되므로
#     if num[i - 1] == int(N[i - 1]):
#         min_sub = 10
#         for j in numbers:
#             if min_sub > abs(j - int(N[i])):
#                 min_sub = abs(j - int(N[i]))
#                 num[i] = j
#     # i 바로 전이 N에 있는 숫자보다 작으면 가장 높은 수가 와야 차가 작아지므로
#     elif num[i - 1] < int(N[i - 1]) or N[i] == '0':
#         num[i] = max(numbers)
#     # 반대이면 가장 작은 수가 와야하므로
#     else:
#         num[i] = min(numbers)

# # num을 다시 정수로 바꾸어주고 총 누르는 버튼 수를 구하면
# new_num = ''
# for k in num:
#     new_num += str(k)
# num = int(new_num)

# push_num = len(N) + abs(num - int(N))

# print(min(from_h, push_num))




min_sub = 500000
num = ''
i = 0
# numbers로 만들 수 있는 숫자를 모두 만들어 가장 N과 차가 작은 것 찾기
def makenum(i, num):
    global min_sub
    if i == len(N):
        if min_sub > abs(int(N) - int(num)):
            min_sub = abs(int(N) - int(num))
            # 만약 num이 N보다 자릿수가 적게 된다면 밑에 len(N)에서 1이
            # 더 더해진게 되므로
        return
    for j in range(10 - M):
        makenum(i + 1, num + str(numbers[j]))

makenum(i, num)
# 최소 버튼 누르는 횟수는
push_num = min_sub + len(N)

# 둘 중 최솟값
print(min(from_h, push_num))