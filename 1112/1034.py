# from copy import deepcopy

# def dfs(i, K, l):
#     global max_cnt
#     if i == K:
#         narr = deepcopy(arr)
#         # print(lst)
#         # print(narr)
#         cnt = 0
#         # 각 행에 대해서 바꾸기
#         for r in range(N):
#             for i in range(M):
#                 if lst[i] == 1:
#                     if narr[r][i] == 0:
#                         narr[r][i] = 1
#                     else:
#                         narr[r][i] = 0
#             # 다 바꿨으면 켜진 행의 개수 찾기
#             if narr[r].count(0) == 0:
#                 cnt += 1
#         max_cnt = max(max_cnt, cnt)
#         return
    
#     # 재귀로 조합 찾기
#     for j in range(l, M):
#         if lst[j] == 0:
#             lst[j] = 1
#             dfs(i + 1, K, j + 1)
#             lst[j] = 0
    

# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# K = int(input())

# # 어차피 짝수번 누르면 똑같으므로 K가 M보다 크면 누르는 열은 의미가 없으므로
# # 최대 M부터 시작해서 2씩 작게 만들어서 그 개수만큼 열을 누른다고 생각하고
# # 조합과 부르트포스를 사용해서 켜져있는 램프를 찾는 식으로 만들면
# if K > M:
#     if (K % 2 == 0 and M % 2 == 0) or (K % 2 == 1 and M % 2 == 1):
#         K = M
#     else:
#         K = M - 1

# i = 0
# max_cnt = 0
# # 누르는 행의 개수가 0개 이상일 동안 계속 반복
# while K - i >= 0:
#     lst = [0] * M
#     dfs(0, K - i, 0)
#     i += 2
    
# print(max_cnt)


# 결국 난 패배했다 아니 이런 생각을 어케하냐 진짜 천재다 천재 난 바보다 바보
# 멍청한 녀석 아오 진짜 ㅁ;ㄴㅇ로밍라훔나어후밀ㅇ햐ㅗㄹ밓ㄶ라멓리ㅑㅎㄹㅇ뭏ㅇㅁ
# 입력받기
n, m = tuple(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(input())
    
k = int(input())

max_cnt = 0

# 모든 행에 대해 반복
for col in range(n):
    # 0의 개수 세기
    zero_count = 0
    for num in lst[col]:
        if num == '0':
            zero_count += 1
        
    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_light_cnt = 0
    if zero_count <= k and zero_count%2 == k%2:  # 이 행을 모두 킬 수 있다면
        for col2 in range(n):  # 다시한번 행을 반복하면서
            if lst[col] == lst[col2]:  # 두 개의 행이 같으면
                col_light_cnt += 1  # 1을 더해준다
                
    max_cnt = max(max_cnt, col_light_cnt)  # 최대값보다 크면 업데이트
    
print(max_cnt)