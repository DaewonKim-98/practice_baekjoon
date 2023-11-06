dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(r, c):
    global max_cnt
    # 0의 개수
    cnt_0 = 0
    # 2의 개수
    cnt_2 = 1
    q = []
    visited[r][c] = 1
    # 0의 방문
    visited0 = [[0] * M for _ in range(N)]
    q.append((r, c))
    list_0 = []

    while q:
        r, c = q.pop(0)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
                cnt_0 += 1
                visited0[nr][nc] = 1
                list_0.append((nr, nc))
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2:
                cnt_2 += 1
                visited[nr][nc] = 1
                q.append((nr, nc))
                
    # 0의 개수가 2개 이하면 상대 돌을 죽일 수 있는데 연결된 2가 더 있으면서 또 연결된 0이 없으면
    # 더 많은 돌을 죽일 수 있으므로
    if cnt_0 == 2:
        if max_cnt < cnt_2:
            max_cnt = cnt_2
        # 0에서 연결된 2가 있으면
        q = []
        visited2 = [[0] * M for _ in range(N)]
        for r, c in list_0:
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and visited2[nr][nc] == 0 and arr[nr][nc] == 2:
                    visited2[nr][nc] = 1
                    q.append((nr, nc))
                    
        cnt_2 += len(q)
        # 여기 2들에 대한 bfs
        while q:
            r, c = q.pop(0)
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
                    cnt_0 += 1
                    visited0[nr][nc] = 1
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2 and visited2[nr][nc] == 0:
                    cnt_2 += 1
                    visited2[nr][nc] = 1
                    q.append((nr, nc))
            # 0의 개수가 2개가 넘어가면 안된다는 것이므로
            if cnt_0 > 2:
                break
        if cnt_0 == 2:
            if max_cnt < cnt_2:
                max_cnt = cnt_2

    # 0의 개수가 1개이면 또 연결된 것을 찾기
    elif cnt_0 == 1:
        if max_cnt < cnt_2:
            max_cnt = cnt_2
        # 0에서 연결된 0들을 모두 찾기
        q = list_0[:]
        visited00 = [[0] * M for _ in range(N)]
        visited00[q[0][0]][q[0][1]] = 1

        while q:
            r, c = q.pop(0)
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 2 and visited00[nr][nc] == 0:
                    list_0.append((nr, nc))
                    q.append((nr, nc))
                    visited00[nr][nc] = 1
        
        # print(list_0)
        visited2 = [[0] * M for _ in range(N)]
        if list_0:
            # 0들에서 연결된 2가 있으면
            q = []
            for r, c in list_0:
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and visited2[nr][nc] == 0 and arr[nr][nc] == 2:
                        visited2[nr][nc] = 1
                        q.append((nr, nc))
            cnt_2 += len(q)
            list_00 = []
            # 여기 2들에 대한 bfs
            while q:
                r, c = q.pop(0)
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
                        cnt_0 += 1
                        list_00.append((nr, nc))
                        visited0[nr][nc] = 1
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2 and visited2[nr][nc] == 0:
                        cnt_2 += 1
                        visited2[nr][nc] = 1
                        q.append((nr, nc))
                # 0의 개수가 2개가 넘어가면 안된다는 것이므로
                if cnt_0 > 2:
                    break
            if cnt_0 == 2:
                if max_cnt < cnt_2:
                    max_cnt = cnt_2
                # 만약 다음 0일 때에도 2가 있다면 그 부분도 봐주어야 하므로
                if list_00:
                    q = []
                    for d in dir:
                        nr, nc = list_00[0][0] + d[0], list_00[0][1] + d[1]
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and visited2[nr][nc] == 0 and arr[nr][nc] == 2:
                            visited2[nr][nc] = 1
                            q.append((nr, nc))
                    cnt_2 += len(q)
                    # 여기 2들에 대한 bfs
                    while q:
                        r, c = q.pop(0)
                        for d in dir:
                            nr, nc = r + d[0], c + d[1]
                            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
                                cnt_0 += 1
                                visited0[nr][nc] = 1
                            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2 and visited2[nr][nc] == 0:
                                cnt_2 += 1
                                visited2[nr][nc] = 1
                                q.append((nr, nc))
                        # 0의 개수가 2개가 넘어가면 안된다는 것이므로
                        if cnt_0 > 2:
                            break
                    if cnt_0 == 2:
                        if max_cnt < cnt_2:
                            max_cnt = cnt_2

        # # 연결된 0이 없을 때 연결된 2가 있으면
        # else:
        #     for d in dir:
        #         nr, nc = list_0[0][0] + d[0], list_0[0][1] + d[1]
        #         if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and visited2[nr][nc] == 0 and arr[nr][nc] == 2:
        #             visited2[nr][nc] = 1
        #             q.append((nr, nc))
        #     # print(q)
        #     list_0 = []
        #     cnt_2 += len(q)
        #     # 여기 2들에 대한 bfs
        #     while q:
        #         r, c = q.pop(0)
        #         for d in dir:
        #             nr, nc = r + d[0], c + d[1]
        #             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
        #                 cnt_0 += 1
        #                 visited0[nr][nc] = 1
        #                 list_0.append((nr, nc))
        #             if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2 and visited2[nr][nc] == 0:
        #                 cnt_2 += 1
        #                 visited2[nr][nc] = 1
        #                 q.append((nr, nc))
        #         # 0의 개수가 2개가 넘어가면 안된다는 것이므로
        #         if cnt_0 > 2:
        #             break
        #     if cnt_0 <= 2:
        #         if max_cnt < cnt_2:
        #             max_cnt = cnt_2
        #         # 만약 다음 0일 때에도 2가 있다면 그 부분도 봐주어야 하므로
        #         if list_0:
        #             q = []
        #             for d in dir:
        #                 nr, nc = list_0[0][0] + d[0], list_0[0][1] + d[1]
        #                 if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and visited2[nr][nc] == 0 and arr[nr][nc] == 2:
        #                     visited2[nr][nc] = 1
        #                     q.append((nr, nc))
        #             cnt_2 += len(q)
        #             # 여기 2들에 대한 bfs
        #             while q:
        #                 r, c = q.pop(0)
        #                 for d in dir:
        #                     nr, nc = r + d[0], c + d[1]
        #                     if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited0[nr][nc] == 0:
        #                         cnt_0 += 1
        #                         visited0[nr][nc] = 1
        #                     if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 2 and visited2[nr][nc] == 0:
        #                         cnt_2 += 1
        #                         visited2[nr][nc] = 1
        #                         q.append((nr, nc))
        #                 # 0의 개수가 2개가 넘어가면 안된다는 것이므로
        #                 if cnt_0 > 2:
        #                     break
        #             if cnt_0 == 2:
        #                 if max_cnt < cnt_2:
        #                     max_cnt = cnt_2

               

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문한 곳 표시
visited = [[0] * M for _ in range(N)]

# 배열을 돌면서 bfs를 통해 2인 구간을 찾고 또 그것과 연결된 1과 2가 아닌 0인 개수를 찾아
# 결국 그 0의 개수가 2개이면 죽일 수 있다는 것이므로 그 개수들 중에서 최대 개수 출력
max_cnt = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] == 2 and visited[r][c] == 0:
            bfs(r, c)

print(max_cnt)