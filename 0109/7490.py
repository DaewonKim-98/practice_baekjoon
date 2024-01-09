def dfs(i, expression):
    if i == N:
        # expression을 돌면서 계산해서 0이 되는지 확인
        result = 0
        num1 = ''
        j = 0
        while j != len(expression):
            # 연산자가 나오면 다음 연산자가 나오거나 끝날 때까지 숫자 더하기
            if expression[j] == '+':
                if len(num1) > 0:
                    result = int(num1)
                    num1 = ''
                j += 1
                num2 = ''
                while expression[j] != '+' and expression[j] != '-':
                    if expression[j] == ' ':
                        j += 1
                        continue
                    num2 += expression[j]
                    j += 1
                    if j == len(expression):
                        break
                result += int(num2)
            elif expression[j] == '-':
                if len(num1) > 0:
                    result = int(num1)
                    num1 = ''
                j += 1
                num2 = ''
                while expression[j] != '+' and expression[j] != '-':
                    if expression[j] == ' ':
                        j += 1
                        continue
                    num2 += expression[j]
                    j += 1
                    if j == len(expression):
                        break
                result -= int(num2)
            else:
                if expression[j] == ' ':
                    j += 1
                    continue
                num1 += expression[j]
                j += 1
        if len(num1) == 0:
            if result == 0:
                arr.append(expression)
        return
    
    for j in range(3):
        if j == 0:
            dfs(i + 1, expression + '+' + str(i + 1))
        elif j == 1:
            dfs(i + 1, expression + '-' + str(i + 1))
        else:
            dfs(i + 1, expression + ' ' + str(i + 1))
        

T = int(input())
for case in range(1, T + 1):
    N = int(input())

    # dfs를 통해 0이 되는 수식 찾기
    arr = []
    dfs(1, '1')
    arr.sort()
    for i in arr:
        print(i)
    print()