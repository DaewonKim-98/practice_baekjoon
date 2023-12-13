N = int(input())

# 학생 리스트
arr = []
for _ in range(N ** 2):
    a, b, c, d, e = map(int, input().split())
    arr.append([a, b, c, d, e])
# 교실
school = [[0] * N for _ in range(N)]

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 각 학생에 대해서 교실을 돌면서 주위에 좋아하는 학생과 빈칸의 개수를 세고
# 최댓값에 그 학생을 두면 될 듯
for student in arr:
    # 좋아하는 학생의 수와 빈칸의 수의 가중치를 다르게 둬서 좋아하는 학생 수를
    # 먼저 판단할 수 있도록 만들기
    max_value = -1
    max_rc = ()
    for r in range(N):
        for c in range(N):
            like_cnt = 0
            blank_cnt = 0
            # 빈자리일 때
            if school[r][c] == 0:
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < N:
                        # 좋아하는 사람이 인접해있으면
                        if school[nr][nc] in student[1:]:
                            like_cnt += 1
                        # 빈칸이 인접해있으면
                        if school[nr][nc] == 0:
                            blank_cnt += 1
                if max_value < like_cnt * 5 + blank_cnt:
                    max_value = like_cnt * 5 + blank_cnt
                    # print(student)
                    # print(max_value)
                    # print(r, c)
                    max_rc = (r, c)
                
    # 그 지점에 그 학생 두기
    school[max_rc[0]][max_rc[1]] = student[0]
# print(school)
    
# 만족도 총합 구하기
dic = {}
for i in arr:
    dic[i[0]] = i[1:]
manjok = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                # 친한 친구가 있으면 개수 세기
                if school[nr][nc] in dic[school[r][c]]:
                    cnt += 1
        if cnt == 0:
            pass
        else:
            manjok += 10 ** (cnt - 1)
        
print(manjok)