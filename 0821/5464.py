import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
park_list = deque([int(input().strip()) for _ in range(N)])
car_list = deque([int(input().strip()) for _ in range(M)])
sequence_list = deque([int(input().strip()) for _ in range(M * 2)])

# 주차장의 번호 리스트
park_idx = deque(range(N))
# 수입
income = 0
# 차량들의 출입 순서의 인덱스를 나타내는
i = 0
# 차량 대기 장소
queue = deque()
# 주차 공간의 인덱스와 차량 번호를 묶을 딕셔너리
car_num = {}
# 차들이 주차장에 들어오는 횟수
cnt = 0
# 차들이 모두 들어올 때까지 while문을 반복
while cnt < M:
    # 출입 순서가 음수면 차량이 나간다.
    if sequence_list[i] < 0:
        # park_list에 다시 차량이 나간 자리의 요금 추가
        park_idx.append(car_num[car_list[-sequence_list[i] - 1]])
        park_idx = sorted(park_idx)
        park_idx = deque(park_idx)
        car_num.pop(car_list[-sequence_list[i] - 1])
        # 차량 대기 장소에 차량이 있으면
        if queue:
            # 차량 대기 장소에 있는 차량을 그대로 가지고 온다.
            c = queue.popleft()
            p = park_idx.popleft()
            car_num[c] = p
            cnt += 1
            income += c * park_list[p]
        i += 1
    # 출입 순서가 양수면 차량이 들어온다.
    elif sequence_list[i] > 0:
        # 차량이 가득 찼으면 i 추가 queue에 차량 추가
        if len(car_num) == N:
            queue.append(car_list[sequence_list[i] - 1])
            i += 1
        # 차량이 가득 차지 않았으면 주차장에 차량 추가
        else:
            p = park_idx.popleft()
            car_num[car_list[sequence_list[i] - 1]] = p
            cnt += 1
            income += car_list[sequence_list[i] - 1] * park_list[p]
            i += 1
print(income)