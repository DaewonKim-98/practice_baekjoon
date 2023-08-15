N = int(input())
arr = list(input())
plist = [int(input()) for _ in range(N)]

stack = []
# 들어온 arr에 대해 반복을 돌린다.
for word in arr:
    # 연산자가 아니면 피연산자에 맞는 인덱스 아스키코드를 이융헤 찾아서 출력
    if word not in '+*/-':
        stack.append(plist[ord(word) - 65])
    # 각 연산자에 대해 연산
    elif word == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif word == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif word == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif word == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)

result = stack[0]
print(f'{result:.2f}')