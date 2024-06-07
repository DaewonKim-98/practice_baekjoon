import sys
sys.setrecursionlimit(100000)

def dfs(i):
    global cnt
    # 왼쪽부터 순회
    if tree[i][0] != -1:
        cnt += 1
        dfs(tree[i][0])
        # 순회 했으면 다시 올라온 것이므로
        cnt += 1
    if tree[i][1] != -1:
        cnt += 1
        dfs(tree[i][1])
        cnt += 1

def rdfs(i):
    global cnt
    if tree[i][1] != -1:
        cnt -= 1
        rdfs(tree[i][1])

    
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]
# print(tree) 
# 1번 노드에서 시작해서 dfs로 이동 횟수 찾기
cnt = 0
dfs(1)

# 1의 오른쪽으로만 가는 것들
rdfs(1)

print(cnt)