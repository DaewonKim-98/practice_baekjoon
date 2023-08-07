N = int(input())

arr = []
for i in range(N):
    arr += [list(map(int, input().split()))]
    

# 같은 반이 최대로 많은 사람의 인덱스를 max_same_idx
max_same_idx = 0
# 같은 반의 수의 최댓값을 max_same
max_same = 0
# 각 학생들를 돌면서 각 학년에 대해 자신과 같은 반을 센다.
for student in range(N):
    same = 0
    # 한번이라도 같은 반을 했으면 다시 같은 반이더라도 중복에서 제외되어야 하므로
    was_same = []
    # 각 학년별로 돌아야 하므로 열 우선 탐색
    for c in range(5):
        for r in range(N):
            # 중복 제외
            if r not in was_same:
                # 만약 각 학생에 맞게 같은 반이 있으면 same에 1 추가
                if arr[r][c] == arr[student][c]:
                    same += 1
                    was_same += [r]
    # 최댓값과 최댓값 인덱스 갱신
    if max_same < same:
        max_same = same
        max_same_idx = student
    
# 인덱스는 학생보다 1 작으므로
print(max_same_idx + 1)