N = int(input())
arr = [i for i in range(1, N + 1)]
linkList = [set()] + []
link = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    linkList.append(set([a, b]))
    link[a].append(b)
    link[b].append(a)
    
    
# 가장 하단이면 no, 중간이면 yes
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        # link에서 연결된게 1개밖에 없으면 가장 하단
        if len(link[k]) == 1:
            print('no')
        else:
            print('yes')
    if t == 2:
        print('yes')
        
        