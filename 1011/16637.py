def dfs(i, operator):
    global max_num
    if i == N - 1:
        num = result[i]
        if max_num < num:
            max_num = num
        return
    # i가 홀수일 때 연산자이므로
    if i % 2 == 1:
        # i가 3 이상일 때 앞의 연산자가 괄호가 있으면 자신은 괄호를 붙일 수 없으므로
        if i >= 3:
            if gwal[i - 2] == 1:
                if arr[i] == '+':
                    result[i + 1] = result[i - 1] + int(arr[i + 1])
                    dfs(i + 1, '+')
                elif arr[i] == '-':
                    result[i + 1] = result[i - 1] - int(arr[i + 1])
                    dfs(i + 1, '-')
                else:
                    result[i + 1] = result[i - 1] * int(arr[i + 1])
                    dfs(i + 1, '*')
            # 앞의 연산자에 괄호가 없으면 자신은 괄호를 붙여도 되므로 괄호를 붙인다는 건 앞의 연산자를
            # 반대로 해준 뒤 자신을 연산한 다음 다시 앞의 연산을 하는 것이므로
            else:
                # 괄호 붙이기
                if operator == '+':
                    gwal[i] = 1
                    if arr[i] == '+':
                        result[i + 1] = result[i - 3] + (int(arr[i - 1]) + int(arr[i + 1]))
                        dfs(i + 1, '+')
                    elif arr[i] == '-':
                        result[i + 1] = result[i - 3] + (int(arr[i - 1]) - int(arr[i + 1]))
                        dfs(i + 1, '-')
                    else:
                        result[i + 1] = result[i - 3] + (int(arr[i - 1]) * int(arr[i + 1]))
                        dfs(i + 1,  '*')
                # 괄호 붙이기
                elif operator == '-':
                    gwal[i] = 1
                    if arr[i] == '+':
                        result[i + 1] = result[i - 3] - (int(arr[i - 1]) + int(arr[i + 1]))
                        dfs(i + 1, '+')
                    elif arr[i] == '-':
                        result[i + 1] = result[i - 3] - (int(arr[i - 1]) - int(arr[i + 1]))
                        dfs(i + 1, '-')
                    else:
                        result[i + 1] = result[i - 3] - (int(arr[i - 1]) * int(arr[i + 1]))
                        dfs(i + 1, '*')
                # 괄호 붙이기
                elif operator == '*':
                    gwal[i] = 1
                    if arr[i] == '+':
                        result[i + 1] = result[i - 3] * (int(arr[i - 1]) + int(arr[i + 1]))
                        dfs(i + 1, '+')
                    elif arr[i] == '-':
                        result[i + 1] = result[i - 3] * (int(arr[i - 1]) - int(arr[i + 1]))
                        dfs(i + 1, '-')
                    else:
                        result[i + 1] = result[i - 3] * (int(arr[i - 1]) * int(arr[i + 1]))
                        dfs(i + 1, '*')
                # 괄호를 안붙이고 연산해도 되므로
                gwal[i] = 0
                if arr[i] == '+':
                    result[i + 1] = result[i - 1] + int(arr[i + 1])
                    dfs(i + 1, '+')
                elif arr[i] == '-':
                    result[i + 1] = result[i - 1] - int(arr[i + 1])
                    dfs(i + 1, '-')
                else:
                    result[i + 1] = result[i - 1] * int(arr[i + 1])
                    dfs(i + 1, '*')
        # i가 1일 때
        else:
            if arr[i] == '+':
                result[i + 1] = int(arr[i - 1]) + int(arr[i + 1])
                dfs(i + 1, '+')
            elif arr[i] == '-':
                result[i + 1] = int(arr[i - 1]) - int(arr[i + 1])
                dfs(i + 1, '-')
            else:
                result[i + 1] = int(arr[i - 1]) * int(arr[i + 1])
                dfs(i + 1, '*')
            
    # i가 짝수일 때는 연산자가 아니므로 그냥 패스
    else:
        dfs(i + 1, operator)


N = int(input())
arr = list(input())

# 처음부터 시작하면서 dfs를 통해 풀기
i = 0
num = 0
operator = 0
# 괄호를 넣었는지 판단
gwal = [0] * N
# 결과 값을 넣을 리스트
result = [0] * N
result[0] = int(arr[0])
max_num = -(2 ** 31)
dfs(i, operator)

print(max_num)