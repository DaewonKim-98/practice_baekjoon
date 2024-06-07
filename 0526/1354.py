def dfs(i):
    if i <= 0:
        return 1
    if i in dic:
        return dic[i]
    a = dfs(i // P - X)
    b = dfs(i // Q - Y)
    dic[i] = a + b
    return a + b

N, P, Q, X, Y = map(int, input().split())

# dfs로?
dic = {}
print(dfs(N))