import sys
input = sys.stdin.readline

V, E, R = map(int, input().split())

e_list = []
for i in range(E):
    e_list.append(list(map(int, input().split())))

# 간선을 오름차순으로 정렬
e_list.sort()

def dfs(V, e_list, R):
    visited_list = [R]
    visited = [0] * (V + 1)
    
    while True:
        # 만약 연결되는 정점이 간선 집합에 있다면
        for e in e_list:
            if R == e[0] and visited[R] == 0:
                R = e[1]
                visited[R] = 1
                visited_list.append(R)
                print(R)
                break
        # 만약 연결되는 정점이 없거나 방문한 적이 있으면
        else:
            # 더 방문할 것이 없는 경우는 0을 출력하므로
            visited_list.append(0)
            break
    return visited_list

for i in dfs(V, e_list, R):
    print(i)