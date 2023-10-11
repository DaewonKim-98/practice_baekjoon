# 순열
def make_num(i):
    global max_num
    if i == len(A):
        # print(p)
        if int(''.join(p)) < B:
            max_num = max(max_num, int(''.join(p)))
        return
    for j in range(len(A)):
        # print(i, A[j])
        # 0으로 시작하면 안된다고 했으므로
        if i == 0 and A[j] == '0':
            # print(0)
            continue
        if visited[j] == 0:
            visited[j] = 1
            p[i] = A[j]
            make_num(i + 1)
            visited[j] = 0

A, B = map(int, input().split())
A = list(str(A))

# 순열로 A 만들기
i = 0
p = [0] * len(A)
visited = [0] * len(A)
max_num = -1
make_num(i)

print(max_num)