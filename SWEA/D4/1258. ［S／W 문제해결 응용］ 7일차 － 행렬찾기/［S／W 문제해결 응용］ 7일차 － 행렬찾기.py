T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행렬리스트
    matrix = []
    # 방문한 곳
    visited = [[0] * N for _ in range(N)]
    # 행을 돌면서 행렬 찾기
    for r in range(N):
        for c in range(N):
            # 행과 열의 길이
            r_length = 0
            c_length = 0
            # 만약 0이 아닌 부분이 나타나면
            if arr[r][c] != 0 and visited[r][c] == 0:
                # 0이 나올 때까지 행과 열을 돌리면서 길이를 찾는다.
                l = 0
                while r + l < N and arr[r + l][c] != 0:
                    l += 1
                    r_length += 1
                l = 0
                while c + l < N and arr[r][c + l] != 0:
                    l += 1
                    c_length += 1
                matrix.append([r_length, c_length])

                # 행렬을 모두 방문했다고 표시
                for i in range(r_length):
                    for j in range(c_length):
                        visited[r + i][c + j] = 1


    matrix.sort(key=lambda x : x[0])
    matrix.sort(key=lambda x : x[0] * x[1])
    print(f'#{case} {len(matrix)}', end=' ')
    for m in matrix:
        print(*m, end=' ')
    print()

