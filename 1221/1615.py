import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def update(start, end, index):
    if end < j - 1 or j - 1 < start:
        return
    
    segment_tree[index] += 1

    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, index * 2)
    update(mid + 1, end, index * 2 + 1)
    
def find(start, end, index):
    if end < j or N - 1 < start:
        return 0
    
    if j <= start and end <= N - 1:
        return segment_tree[index]
    
    mid = (start + end) // 2
    return find(start, mid, index * 2) + find(mid + 1, end, index * 2 + 1)

# arr = [list(map(int, input().strip().split())) for _ in range(M)]
# # 정렬하면 왼쪽은 자동으로 정렬 되니까 오른쪽에서 작아지면 간선이 생기는 것 같은데
# arr.sort()

dic = {}
for _ in range(M):
    a, b = map(int, input().strip().split())
    if a in dic:
        dic[a].add(b)
    else:
        dic[a] = set([b])
   
        
segment_tree = [0] * (N * 4)

cnt = 0
for k in range(1, N + 1):
    if k in dic:
        arr = list(dic[k])
        arr.sort()
        for j in arr:
            # j보다 큰 놈들의 누적합이라고 생각하면 어차피 정렬되어 있으니까 
            # 같은 i끼리는 안볼꺼고 자기 이전에 자기보다 큰 것들의 누적합을 찾으면 되므로
            # j부터 N - 1까지의 누적합을 구하면 간선의 총 교차 개수를 구할 수 있다
            # 자신의 개수를 누적합으로 업데이트 해주기
            # print(segment_tree)
            update(0, N - 1, 1)
            cnt += find(0, N - 1, 1)
            # print(cnt)

# print(segment_tree)
print(cnt)