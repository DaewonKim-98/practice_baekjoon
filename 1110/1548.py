N = int(input())
arr = list(map(int, input().split()))
arr.sort()

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(2)
    exit()
# ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# 재귀로 절대 안됨
# for 문으로 처음과 끝 판단, 처음 2개와 끝을 판단하면 됨
length = 0
for i in range(N - 2):
    for j in range(N - 1, -1, -1):
        if arr[i] + arr[i + 1] > arr[j]:
            length = max(length, j - i + 1)

print(length)