import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# 4번 타자를 빼고 나머지 타자의 타순
sequence = [1, 2, 3, 4, 5, 6, 7, 8]
sequences = set(permutations(sequence))

# 돌면서 최대 점수 확인
max_score = 0
for p in sequences:
    i = -1
    score = 0
    p = list(p)
    p.insert(3, 0)
    for s in range(N):
        out = 0
        # 1루, 2루, 3루
        base = [0, 0, 0]
        # 타순대로 점수
        while out < 3:
            i += 1
            # print(i, arr[s][p[i]], end=' ')
            # print(score)
            if i == 9:
                i = 0
            # 아웃이면 아웃 횟수 1 추가
            if arr[s][p[i]] == 0:
                out += 1
            
            # 1루타
            elif arr[s][p[i]] == 1:
                score += base[2]
                base = [1, base[0], base[1]]
                    
            # 2루타
            elif arr[s][p[i]] == 2:
                score += base[2] + base[1]
                base = [0, 1, base[0]]
                    
            # 3루타
            elif arr[s][p[i]] == 3:
                score += base[2] + base[1] + base[0]
                base = [0, 0, 1]
                
            # 홈런
            else:
                score += base[2] + base[1] + base[0] + 1
                base = [0, 0, 0]
            
    # if score > 0:
        # print(p)
        # print(score)
    max_score = max(max_score, score)
    
print(max_score)