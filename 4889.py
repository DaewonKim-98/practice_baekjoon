i = 1

while True:
    lst = list(input())
    if '-' in lst:
        break
    # 열린 괄호의 수만큼 닫힌 괄호 필요
    open = 0
    cnt = 0
    for j in range(len(lst)):
        # 열린 괄호가 나오면
        if lst[j] == '{':
            open += 1
        # 닫힌 괄호가 나왔을 때 열린 괄호가 없으면 바꿔줘야 하므로
        if lst[j] == '}':
            if open == 0:
                open += 1
                cnt += 1
            # 앞에 열린 괄호가 있으면 닫기
            else:
                open -= 1
    # 다 끝났을 때도 괄호가 열려 있으면 안닫은 것이 있다는 것이므로
    cnt += open // 2
    print(f'{i}. {cnt}')
    i += 1