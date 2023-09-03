import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input().strip())

# 가로를 나타내는 리스트와 세로를 나타내는 리스트
a_list = [0] * (A + 1)
b_list = [0] * (B + 1)

for i in range(N):
    c, d = map(int, input().split())
    if c == 1:
        a_list[d] = 1
    else:
        b_list[d] = 1

# 가장 앞부분은 개수에서 셀 필요가 없으므로 잘라낸다.
a_list.pop(0)
b_list.pop(0)
# 길이 리스트를 만든다.        
a_length_list = []
b_length_list = []

# 0이 연속으로 있는 부분이 길이이므로 1이 나오면 지금까지 0인 부분을 길이 리스트에 추가
cnt = 0
for i in range(A):
    cnt += 1
    if a_list[i] == 1 or i == A - 1:
        a_length_list.append(cnt)
        cnt = 0

cnt = 0
for i in range(B):
    cnt += 1
    if b_list[i] == 1 or i == B - 1:
        b_length_list.append(cnt)
        cnt = 0

max_area = 0
# 가로와 세로 리스트에서 각 길이를 곱한 리스트를 만들고 최댓값 출력    
for a_length in a_length_list:
    for b_length in b_length_list:
        if max_area < a_length * b_length:
            max_area = a_length * b_length
            
print(max_area)