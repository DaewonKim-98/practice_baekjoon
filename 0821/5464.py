import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
park_list = deque([int(input().strip()) for _ in range(N)])
car_list = deque([int(input().strip()) for _ in range(M)])
sequence_list = deque([int(input().strip()) for _ in range(M * 2)])

# 주차장과 주차장에 주차하는 차 번호와 주차장 딕셔너리
park_idx = list(range(N))
parking = dict()
# 대기 중인 차량이 있는 큐
queue = deque()
# 수입
income = 0

# 주차장 출입 순서를 돌리면서 차량 주차
for sequence in sequence_list:
    if sequence > 0:
        # 차가 꽉 찼으면 큐로 보낸다.
        if len(parking) == N:
            queue.append(sequence)
        # 공간이 남아 있으면 주차장의 번호 리스트와 주차하는 차 번호를 딕셔너리에
        else:
            # 주차 공간을 없애고
            p = park_idx.pop(0)
            # 주차된 공간 딕셔너리에 추가
            parking[sequence] = p
            # 수입은 차의 무게와 주차 공간의 단위 무게당 요금의 곱
            income += car_list[sequence - 1] * park_list[p]
    # 순서가 음수로 나오면
    else:
        # 주차장에 다시 공간을 추가하고
        park_idx.append(parking[-sequence])
        # 주차 순서대로 다시 정렬
        park_idx.sort()
        # 딕셔너리에서 순서를 pop
        parking.pop(-sequence)
        # 대기중인 차량이 있으면
        if queue:
            # 위에와 마찬가지로 대기중의 차량 가장 앞을 없애고
            sequence = queue.popleft()
            # 주차 공간을 없애고
            p = park_idx.pop(0)
            # 딕셔너리에 추가 후
            parking[sequence] = p
            # 수입 계산
            income += car_list[sequence - 1] * park_list[p]
print(income)