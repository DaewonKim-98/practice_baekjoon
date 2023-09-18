import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

expression = input().strip()
operator = ['+', '-']
# 식이 최소가 되려면 - 연산자가 나오면 이후는 모두 -로 연산해주면 됨
plus_calculate = 0
minus_calculate = 0
num = ''
minus = False
for i in range(len(expression)):
    # 연산자가 나올 때까지 num을 만들기
    if expression[i] not in operator:
        num += expression[i]
    # 마이너스가 나오면 마이너스가 나왔다고 해주고 마이너스에 합
    elif expression[i] == '-':
        # 마이너스가 한번도 안나왔으면
        if minus == False:
            plus_calculate += int(num)
            num = ''
    # 마이너스가 나왔으면
        elif minus == True:
            minus_calculate += int(num)
            num = ''
        minus = True
    # 플러스가 나오면
    elif expression[i] == '+':
        # 마이너스가 한번도 안나왔으면
        if minus == False:
            plus_calculate += int(num)
            num = ''
    # 마이너스가 나왔으면
        elif minus == True:
            minus_calculate += int(num)
            num = ''
    # 마지막까지 도달하면 더하기
    if i == len(expression) - 1:
        # 마이너스가 한번도 안나왔으면
        if minus == False:
            plus_calculate += int(num)
            num = ''
        # 마이너스가 나왔으면
        elif minus == True:
            minus_calculate += int(num)
            num = ''

print(plus_calculate - minus_calculate)