N, P = map(int, input().split())
# 각 줄과 그 줄의 프렛 리스트를 가지는 딕셔너리
dic = {}
for i in range(1, N + 1):
    dic[i] = []

# 프랫을 스택에 넣고 빼기
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    # 줄에 맞는 프렉이 리스트에 하나라도 있거나
    # 리스트에서 가장 마지막 것이 b보다 크면 계속 빼야하므로
    while dic[a] and dic[a][-1] > b:
        cnt += 1
        dic[a].pop()
    # 가장 마지막 것이 b와 같다면 아무것도 안해도 되므로
    if dic[a] and dic[a][-1] == b:
        pass
    else:
        # b보다 작게 되거나 리스트가 비게 되면 b 채우기
        dic[a].append(b)
        cnt += 1
    
print(cnt)