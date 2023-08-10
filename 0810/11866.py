N, K = map(int, input().split())

arr = list(range(1, N + 1))

# 요세푸스 순열
nlist = []
# 순열이 N개가 될 때까지 반복
while len(nlist) < N:
    # 처음 K - 1개를 뒤로 돌리면 0번째 수가 원래의 N 번째 수
    for i in range(K - 1):
        arr.append(arr.pop(0))
    # 순열에 추가하고 arr에서 제거
    nlist.append(str(arr.pop(0)))
result = '<' + ', '.join(nlist) + '>'
print(result)