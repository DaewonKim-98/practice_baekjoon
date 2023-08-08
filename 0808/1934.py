arr = list(map(int, input().split()))
arr.sort()

# 작은게 A, 큰게 B
A = arr[0]
B = arr[1]

# A에서부터 역순으로 i를 만들고
for i in range(A, 0, -1):
    # A 와 B 모두 i로 0으로 나누어떨어지면 최대공약수이므로
    if A % i == 0 and B % i == 0:
        # 최소공배수는
        print((A // i) * B)
        break

