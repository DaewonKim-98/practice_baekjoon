M, N = map(int, input().split())

# 아오 또 시간초과 진짜
# 균등하다는 것은 가장 큰 값이 같은 위치, 각각의 크고 작은 값들이 같은 위치에
# 있다는 것이므로 등수로 만들어서 딕셔너리로 세보기?
dic = {}

for _ in range(M):
    universe = list(map(int, input().split()))
    
    # 중복되는 것 제거해서 각 크기에 따라 등수를 만들 수 있게
    sort_universe = sorted(list(set(universe)))

    # 행성의 각 크기별로 등수 만들기
    rank = {}
    for i in range(len(sort_universe)):
        rank[sort_universe[i]] = i
        
    # 등수를 튜플로 저장해서 그 튜플을 키로 하는 딕셔너리를 만들어서
    # 그 딕셔너리에서 각 키들에 대해 쌍의 개수 출력? 오 미쳤다 설마? 이건가!!!!!!
    rank_universe = []
    for i in range(N):
        rank_universe.append(rank[universe[i]])
    
    # 딕셔너리에 랭크로 된 튜플이 있으면 유니버스 튜플을 세트에 추가
    rank_universe = tuple(rank_universe)
    if rank_universe in dic:
        dic[rank_universe].add(tuple(universe))
    # 없으면 유니버스 튜플을 가지는 세트 만들기
    else:
        dic[rank_universe] = set()
        dic[rank_universe].add(tuple(universe))
        
result = 0
for k, v in dic.items():
    # 쌍은 N개 중에서 2개 고르는 것이므로
    n = len(v)
    result += (n * (n - 1)) // 2

# print(dic)  
print(result)