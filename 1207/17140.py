R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) + [0] * 97 for _ in range(3)] + [[0] * 100 for _ in range(97)]

cnt = 0
if arr[R - 1][C - 1] == K:
    print(0)
    exit()
max_r = 3
max_c = 3
while cnt < 100:
    cnt += 1
    
    # r정렬
    if max_r >= max_c:
        max_length = 0
        for r in range(100):
            if arr[r][0] == 0:
                break
            dic = {}
            for c in range(100):
                if arr[r][c] == 0:
                    break
                if arr[r][c] not in dic:
                    dic[arr[r][c]] = 1
                else:
                    dic[arr[r][c]] += 1

            lst = []
            for k, v in dic.items():
                lst.append([k, v])
            lst.sort(key=lambda x: x[0])
            lst.sort(key=lambda x: x[1])
            
            
            for i in range(50):
                if i < len(lst):
                    arr[r][2 * i] = lst[i][0]
                    arr[r][2 * i + 1] = lst[i][1]
                    max_c = max(max_c, 2 * i + 1 + 1)
                else:
                    arr[r][2 * i] = 0
                    arr[r][2 * i + 1] = 0
            
    # c정렬
    else:
        max_length = 0
        for c in range(100):
            if arr[0][c] == 0:
                break
            dic = {}
            for r in range(100):
                if arr[r][c] == 0:
                    break
                if arr[r][c] not in dic:
                    dic[arr[r][c]] = 1
                else:
                    dic[arr[r][c]] += 1
            lst = []
            for k, v in dic.items():
                lst.append([k, v])
            lst.sort(key=lambda x: x[0])
            lst.sort(key=lambda x: x[1])
            
            for i in range(50):
                if i < len(lst):
                    arr[2 * i][c] = lst[i][0]
                    arr[2 * i + 1][c] = lst[i][1]
                    max_r = max(max_r, 2 * i + 1 + 1)
                else:
                    arr[2 * i][c] = 0
                    arr[2 * i + 1][c] = 0
            
    # print(arr)
    # 정렬이 끝났을 때 k가 되면 i 출력
    if arr[R - 1][C - 1] == K:
        print(cnt)
        exit()

# while문이 끝나도 출력이 안되면
print(-1)