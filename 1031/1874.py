N = int(input())

numbers = list(range(1, N + 1))
sequence = [int(input()) for _ in range(N)]
stack = []
result = []

while sequence:
    # 스택이 비었으면 그냥 추가
    if not stack:
        stack.append(numbers.pop(0))
        result.append('+')
    # 스택의 마지막 값이 수열의 첫 번째보다 작으면 계속 스택 채우기
    if stack[-1] < sequence[0]:
        # 스택이 더 이상 채울 수 없으면 수열을 만들기 불가능하므로
        if not numbers:
            print('NO')
            exit()
        stack.append(numbers.pop(0))
        result.append('+')
    # 스택의 마지막 값이 수열의 첫 번째와 같으면 수열을 만드는 것이므로 제거
    elif stack[-1] == sequence[0]:
        stack.pop()
        sequence.pop(0)
        result.append('-')
    # 더 크면 수열을 만들기 불가능하므로
    elif stack[-1] > sequence[0]:
        print('NO')
        exit()

for i in result:
    print(i)