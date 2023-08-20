import sys
input = sys.stdin.readline

N = int(input().strip())
S, G = map(int, input().split())
m = int(input().strip())

# 연결된 촌수를 나타내는 리스트
m_list = [[] for _ in range(N + 1)]
for i in range(m):
    a, b = map(int, input().split())
    m_list[a].append(b)
    m_list[b].append(a)

# 너비 우선 탐색으로 하나씩 늘려나간다.
def bsf(N, S, G):
    visited = [0] * (N + 1)
    visited[S] = 1
    q = []
    q.append(S)
    
    while len(q) > 0:
        t = q.pop(0)
        # 만약 t가 G가 되면 연결되었고 처음부터 visited를 더했으므로 촌수대로 출력
        if t == G:
            return visited[t] - 1
        # 연결된 간선 중에
        for w in m_list[t]:
            # 방문하지 않았다면
            if visited[w] == 0:
                q.append(w)
                visited[w] += visited[t] + 1

    # 돌렸을 때 G로 출력이 안된다면 -1 출력            
    return -1
print(bsf(N, S, G))
