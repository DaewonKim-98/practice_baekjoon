import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

arr = list(input().strip())

# b의 개수만큼 칸들을 움직이면서 b의 개수가 가장 많은 칸을 찾아
# 나머지 a를 b로 교환하면 그게 가장 작은 교환 횟수가 아닐까?
# 그리고 인덱스를 넘어가면 처음과 끝이 인접해있으므로 앞에 것도 추가해서 생각
# 아니면 컴퓨터 진짜로 뿌술듯

cnt = arr.count('b')
max_cnt = 0
for i in range(len(arr)):
    c = 0
    for j in range(i, i + cnt):
        if j >= len(arr):
            j = j - len(arr)
        # 칸에서 b의 갯수를 세서 가장 많은 b 찾기
        if arr[j] == 'b':
            c += 1
    if max_cnt < c:
        max_cnt = c

# 교환 횟수의 최솟값은
print(cnt - max_cnt)