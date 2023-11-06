T = int(input())
for case in range(1, T + 1):
    arr = input()
    # while로 돌면서 전파인지 아닌지 확인
    a = '100'
    b = '01'
    i = 0
    # 전파
    wave = False
    while i < len(arr):
        # print(i)
        # 01이면 그 이후 봐주기
        if i + 2 <= len(arr) and arr[i:i + 2] == b:
            # 끝까지 갔으면
            if i + 2 == len(arr):
                print('YES')
                wave = True
                break
            i += 2
        # 100이 나오면 나중에 1이 나올 때까지 봐주기
        elif i + 3 <= len(arr) and arr[i:i + 3] == a:
            # 다음 4번째가 1이 아니고 끝이면 전파가 아니므로
            if i + 3 == len(arr):
                print('NO')
                wave = True
                break
            # 4번째가 0이면 1을 찾을 때까지 계속 올리기
            while arr[i + 3] == '0':
                i += 1
                if i + 3 == len(arr):
                    print('NO')
                    wave = True
                    break
            # 4번째가 1이면 다음 0이 나올 때까지 계속 올리기
            while i + 3 < len(arr) and arr[i + 3] == '1':
                i += 1
                # 그런데 올렸을 때 또 100이 나온다면 다시 돌아가야 하므로
                if i + 6 < len(arr) and arr[i + 3:i + 6] == a:
                    break
                # 끝까지 갔으면
                if i + 3 == len(arr):
                    print('YES')
                    wave = True
                    break
            # 다 돌았으면
            i += 3
        else:
            print('NO')
            wave = True
            break
    # 이것들이 안나오면 전파가 아니므로
    if wave == False:
        print('NO')
