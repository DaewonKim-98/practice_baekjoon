from collections import deque

def rot(num, dir):
    copynum = list(gear[num]).copy()
    # 일단 톱니바퀴 돌리기
    gear[num].rotate(dir)
    
    # 왼쪽 톱니바퀴들 확인
    i = num
    original = copynum
    ndir = -dir
    while i > 0:
        # 왼쪽 톱니바퀴와 비교했을 때 극이 다르면
        if original[6] != gear[i - 1][2]:
            # original 갱신하고 톱니바퀴 돌리기
            original = list(gear[i - 1]).copy()
            gear[i - 1].rotate(ndir)
            ndir = -ndir
            i -= 1
        
        # 극이 같으면 회전하지 않으므로
        else:
            break
            
    # 오른쪽 톱니바퀴들 확인
    i = num
    original = copynum
    ndir = -dir
    while i < T - 1:
        # 오른쪽 톱니바퀴와 비교했을 때 극이 다르면
        if original[2] != gear[i + 1][6]:
            # original 갱신하고 톱니바퀴 돌리기
            original = list(gear[i + 1]).copy()
            gear[i + 1].rotate(ndir)
            ndir = -ndir
            i += 1
        
        # 극이 같으면 회전하지 않으므로
        else:
            break

T = int(input())
gear = [deque(map(int, input())) for _ in range(T)]
K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    rot(num - 1, dir)

# 모두 돌린 뒤 12시 방향이 S인 개수 출력
# print(gear)
cnt = 0
for i in gear:
    if i[0] == 1:
        cnt += 1
        
print(cnt)