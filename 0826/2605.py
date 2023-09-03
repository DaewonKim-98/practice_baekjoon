N = int(input())

students = list(range(1, N + 1))
sequence = list(map(int, input().split()))

arr = []
# 뽑은 것에 따라 학생의 줄을 바꾼다.
for i in range(N):
    arr.insert(sequence[i], students[i])
    
# 반대로 줄을 바꾸었으므로 거꾸로 출력
for j in range(N -1, -1, -1):
    print(arr[j], end=' ')