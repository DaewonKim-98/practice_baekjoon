N = int(input())

arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr += [row]

# x좌표에 대해 오름차순으로 정렬        
for j in range(N, 1, -1):
    for k in range(1, j):
        if arr[k - 1][1] > arr[k][1]:
            # arr[k - 1], arr[k] = arr[k], arr[k - 1]
            # y좌표에 대해 오름차순으로 정렬    
            if arr[k - 1][0] > arr[k][0]:
                arr[k - 1], arr[k] = arr[k], arr[k - 1]            
        

# # y좌표에 대해 오름차순으로 정렬        
# for j in range(N, 1, -1):
#     for k in range(1, j):
#         if arr[k - 1][0] == arr[k][0]:
#             if arr[k - 1][1] > arr[k][1]:
#                 arr[k - 1], arr[k] = arr[k], arr[k - 1]            
        
# 정답 출력
for l in arr:
    print(str(l[0]) + ' ' + str(l[1]))