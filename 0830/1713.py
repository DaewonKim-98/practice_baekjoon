import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
students = list(map(int, input().split()))

# 사진틀
picture = []
# 사진틀에서 추천 받은 횟수를 나타내는 리스트
recommend = [0] * N

# 학생 리스트에서 사진틀에 넣고 규칙대로 후보 결정
for s in students:
    # 사진틀에 학생이 있으면 추천 횟수 증가
    if s in picture:
        recommend[picture.index(s)] += 1
    # 사진틀이 N개보다 작으면 사진틀에 추가할 수 있으므로
    elif len(picture) < N:
        picture.append(s)
        recommend[picture.index(s)] += 1
    # 사진틀이 N개이면 비어있는 사진틀이 없으므로
    elif len(picture) == N:
        min_recommend = min(recommend)
        # 학생을 제거하고 추천 횟수도 제거한 뒤 다시 추천 횟수 0 추가
        picture.pop(recommend.index(min_recommend))
        recommend.pop(recommend.index(min_recommend))
        recommend.append(0)
        # 다시 사진틀에 추가
        picture.append(s)
        recommend[picture.index(s)] += 1

picture.sort()
print(*picture)