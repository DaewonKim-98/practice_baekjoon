def dfs(i, j, lst):
    # 다시 자기 자신이 되면 끝이므로
    if i == j:
        answer.extend(lst)
        for i in lst:
            visited[i] = 1
        return
    if j in lst:
        return
    dfs(i, arr[j], lst + [j])
    

N = int(input())
arr =[0] + [int(input()) for _ in range(N)]

# dfs로 타고 타고 계속 갔을때 다시 자기가 나오면 세트로 연결되는 것
answer = []
visited = [0] * (N + 1)
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i, arr[i], [i])
            
print(len(answer))
answer.sort()
for i in answer:
    print(i)