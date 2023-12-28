N = int(input())

arr = [1] * (N + 1)
for i in range(1, N + 1):
    arr[i] = 0
    for j in range(i):
        arr[i] += arr[j] * arr[i - 1 - j]

# print(arr)
print(arr[N])