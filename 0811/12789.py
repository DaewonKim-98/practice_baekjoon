N = int(input())
arr = list(map(int, input().split()))

# 처음 스택은 쓸모 없는 0을 두고 시작한다.
stack = [0]
# 순서는 1부터 시작
sequence = 1
# 처음 줄이 모두 없어질 때까지 반복
while len(arr) > 0:
    # 스택의 마지막 사람이 순서면 그 사람을 없애고 순서를 1 늘린다.
    if stack[-1] == sequence:
        stack.pop()
        sequence += 1
    # 줄의 첫 사람이 순서면 그 사람을 없애고 순서를 1 늘린다.
    elif arr[0] == sequence:
        arr.pop(0)
        sequence += 1
    # 스택의 마지막과 줄의 처음에 순서가 아무도 없으면 
    # 줄의 처음을 스택의 마지막으로 옮긴다
    else:
        person = arr.pop(0)
        stack.append(person)

# 이러면 일단 while 문이 끝나고 arr에 있던 것들은 모두 공간으로 이동했다.
# 그래서 스택에서 거꾸로 나오게 하면 되는데 순서와 다르게 된다면 종료한다.
while True:
    if stack[-1] == sequence:
        stack.pop()
        sequence += 1
    else:
        break

# 모두가 다 끝났을 때 stack 에 원래 있던 0만 있으면 Nice
if len(stack) == 1:
    print('Nice')
else:
    print('Sad')