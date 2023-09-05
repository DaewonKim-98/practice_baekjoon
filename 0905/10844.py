N = int(input())

# 배열 자체를 0이 10개 있는 것으로 만들어서 채워나가고 마지막 N번째에서 합 출력
arr = [[0] * 10 for _ in range(N + 2)]

arr[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    # 자신 이전에서 0과 9를 가는 것 빼고는 2개씩 가능이고 0과 9로 가면 1개씩 밖에 더 못가므로
    arr[i][0] = arr[i - 1][1] 
    arr[i][9] = arr[i - 1][8] 
    for j in range(1, 9):
        arr[i][j] = arr[i - 1][j - 1]  + arr[i - 1][j + 1]
        
print(sum(arr[N]) % 1000000000)