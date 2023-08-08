T = int(input())

for case in range(1, T + 1):
    brackets = list(input())

    # 결과는 YES
    result = 'YES'

    len_brackets = 0
    for i in brackets:
        len_brackets += 1

    # ( 이면 cnt 에 1 추가, ) 면 cnt 에 -1 0 이 되면 똑같다는 것
    cnt = 0
    for j in range(len_brackets):
        if brackets[j] == '(':
            cnt += 1
        else:
            cnt -= 1
        # cnt 가 0보다 작아지면
        if cnt < 0:
            result = 'NO'
            break

    if cnt == 0:
        print(result)
    else:
        print('NO')