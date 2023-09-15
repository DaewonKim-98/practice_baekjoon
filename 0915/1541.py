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
for i in expression:
    # 연산자가 나올 때까지 num을 만들기
    if i not in operator:
        num += i
    # 마이너스가 나오면 마이너스가 나왔다고 해주고 마이너스에 합
    if i == '-':
        minus = True
        minus_calculate += int(num)
        num = ''
    # 마이너스가 한번도 안나왔으면
    if minus == False:
        if i == '+':
            plus_calculate += int(num)
            num = ''
    elif minus == True:
        if i == '+':
            minus_calculate += int(num)
            num = ''