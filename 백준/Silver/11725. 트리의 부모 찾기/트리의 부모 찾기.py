import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 전위 순회
def preorder_travel(n):
    # 간선 리스트에서 보면 ch는 자식
    for ch in e_list[n]:
        # 자식에서 부모로 가는 경우를 제거
        e_list[ch].remove(n)
        # 방문하지 않았으면 자식이므로 (방문 했으면 부모)
        preorder_travel(ch)
        par[ch] = n


N = int(input().strip())
# 간선 리스트
e_list = [[] * (N + 1) for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    e_list[a].append(b)
    e_list[b].append(a)


# 자식을 인덱스로 하는 부모 노드 리스트
par = [0] * (N + 1)
n = 1

preorder_travel(n)
for i in range(2, N + 1):
    print(par[i])