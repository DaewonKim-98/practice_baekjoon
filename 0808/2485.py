N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

sub = 0
# 가로수의 간격의 최댓값은 나누었을 때 나머지가 같은 것이다.
for j in range(1000000000, 0, -1):
    remain = True
    for k in range(len(arr) - 1):
        if arr[k] % j != arr[k + 1] % j:
            remain = False
            break
    # 모든 arr 에서 나누었을 때 나머지가 모두 같다는 것이므로
    if remain == True:
        sub = j
        break

# 가로수의 수는 간격에 따라 다르므로 가장 뒤와 가장 앞의 수를 간격으로 나눈 몫의 차
print(arr[-1] // sub - arr[0] // sub)