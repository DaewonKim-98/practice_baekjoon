V = int(input())
E = int(input())

# 연결된 컴퓨터의 리스트들을 리스트화
elist = []
for i in range(E):
    elist.append(list(map(int, input().split())))

# V에 대한 배열을 만들어 연결되어 잇는 컴퓨터들을 1로 둔다.
arr_v = [[0] * (V + 1) for _ in range(V + 1)]
for e in elist:
    arr_v[e[0]][e[1]] = 1
    arr_v[e[1]][e[0]] = 1

# dfs 함수
def dfs(n, V, arr_v):
    stack = []
    visited = [0] * (V + 1)
    visited[n] = 1

    # 반복을 돌면서 visited로 연결된 부분들을 찾고 stack에 넣었다 뺐다 한다.
    while True:
        for w in range(1, V + 1):
            # 연결된 부분이 있고, 방문한 적이 없다면 stack에 추가하고 n 갱신
            if arr_v[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                break

        # 더 이상 연결된 부분이 없고, 모든 방문을 마쳤으면 
        else:
            # 만약 stack이 남아있으면 위로 올라간다.
            if stack:
                n = stack.pop()

            # 더 이상 스택도 남아있지 않다면 모든 것을 다 돌았다는 것이므로 탈출
            else:
                break
    # 컴퓨터의 수는 방문한 수에서 1번을 뺀 것이므로
    result = visited.count(1) - 1
    return result

print(dfs(1, V, arr_v))