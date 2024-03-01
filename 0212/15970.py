N = int(input())
dic = {}

# 색을 키로 가지는 것들 dic에 추가
for _ in range(N):
    a, b = map(int, input().split())
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]

length = 0  
# 정렬한 다음 화살표 길이 추가
for k, v in dic.items():
    v.sort()
    # 돌면서 좌우에서 가까운 값 찾기
    for i in range(len(v)):
        # 양 끝값은 따로
        if i == 0 and len(v) > 1:
            length += v[1] - v[0]
        elif i == len(v) - 1 and len(v) > 1:
            length += v[-1] - v[-2]
        
        else:
            length += min(v[i] - v[i - 1], v[i + 1] - v[i])
            
print(length)