import sys
input = sys.stdin.readline

T = int(input().strip())
N = int(input().strip())
a_list = [0] + list(map(int, input().split()))
M = int(input().strip())
b_list = [0] + list(map(int, input().split()))

# 누적합으로 구하기?
for i in range(1, N + 1):
    a_list[i] = a_list[i - 1] + a_list[i]
for j in range(1, M + 1):
    b_list[j] = b_list[j - 1] + b_list[j]

# print(a_list)
# print(sum_a_list)
# 각 부분 배열의 합 리스트
a_part_sum = []
for i in range(N):
    for j in range(i + 1, N + 1):
        a_part_sum.append(a_list[j] - a_list[i])
b_part_sum = []
for i in range(M):
    for j in range(i + 1, M + 1):
        b_part_sum.append(b_list[j] - b_list[i])

b_part_sum.sort()
length_b = len(b_part_sum)
# 여기서 이분 탐색을 써야하나? 어케쓰노
# b에 대해 이분탐색 ㄱㄱ?
cnt = 0
# a가 중복되면 계산이 중복되므로 딕셔너리를 만들어 중복되는 a가 있으면 그냥
# 그 값을 cnt에 추가
dic = {}
for a in a_part_sum:
    if a in dic:
        cnt += dic[a]
        continue
    start = 0
    end = length_b - 1
    while start <= end:
        middle = (start + end) // 2
        
        # 중간 값이 T가 되면 cnt 추가해주고
        if a + b_part_sum[middle] == T:
            dic[a] = 1
            cnt += 1
            i = 1
            # 중복되는 값이 있을수도 있으므로 b의 앞 뒤로 또 합이 T가 되는 것 찾기
            if 0 <= middle + i < length_b:
                while a + b_part_sum[middle + i] == T:
                    dic[a] += 1
                    cnt += 1
                    i += 1
                    if middle + i >= length_b:
                        break
            j = 1
            if 0 <= middle - j < length_b:
                while a + b_part_sum[middle - j] == T:
                    dic[a] += 1
                    cnt += 1
                    j += 1
                    if middle - j < 0:
                        break
            break
        # 합이 T보다 작으면 중간값 up
        elif a + b_part_sum[middle] < T:
            start = middle + 1
        else:
            end = middle - 1

print(cnt)
