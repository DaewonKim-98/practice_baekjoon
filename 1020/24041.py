N, G, K = map(int, input().split())
s_list = []
l_list = []
o_list = []
for _ in range(N):
    s, l, o = map(int, input().split())
    s_list.append(s)
    l_list.append(l)
    o_list.append(o)
    
# 구매 후 먹을 수 있는 날짜를 올리면서 언제까지 먹을 수 있는지 찾기
can_eat = True
day = min(l_list)
while can_eat == True:
    k = K
    # 세균 수의 리스트는
    germ_list = [0] * N
    for i in range(N):
        germ_list[i] = (s_list[i] * max(1, day - l_list[i]), o_list[i])
    # 세균 수가 많은 것부터 정렬
    germ_list.sort(reverse=True)
    
    # print(germ_list)
    # day의 총 세균 수
    germ = 0
    for i in range(N):
        germ += germ_list[i][0]
    # 총 세균 수가 G보다 크면 계속 빼기
    i = 0
    while germ > G:
        if germ_list[i][1] == 1:
            germ -= germ_list[i][0]
            k -= 1
            i += 1
        else:
            i += 1
        if k < 0 or (i == N and germ > G):
            can_eat = False
            break
        
    if can_eat == False:
        day -= 1
        break
    else:      
        day += 1
print(day)