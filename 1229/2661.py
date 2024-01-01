def dfs(i, num):
    if i == N:
        print(num)
        exit()
    
    for j in range(3):
        num2 = num + arr[j]
        # 나쁜 수열 찾기
        good = True
        # print(num2)
        for k in range((i - 1) // 2 + 1):
            if num2[-2 -2*k:-1 -k] == num2[-1 -k:]:
                good = False
                break
        # 좋은 수열 그대로면
        if good == True:
            dfs(i + 1, num2)

N = int(input())
arr = ['1', '2', '3']

if N == 1:
    print(1)
    exit()
# dfs를 통해
dfs(1, '1')