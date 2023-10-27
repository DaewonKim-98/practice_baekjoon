T = int(input())
for case in range(1, T + 1):
    N = int(input())
    # 1개면 일관성 있으므로
    if N == 1:
        print('YES')
    else:
        arr = [list(input()) for _ in range(N)]
        arr.sort(key=lambda x: len(x))
        arr.sort()
        # print(arr)
        
        # 정렬했으면 바로 다음 것이랑만 비교해주면 될듯?
        for i in range(0, N - 1):
            same = True
            for j in range(len(arr[i])):
                if arr[i][j] != arr[i + 1][j]:
                    same = False
                    break
            if same == True:
                print('NO')
                break
        else:
            print('YES')