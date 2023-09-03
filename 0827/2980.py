import sys
input = sys.stdin.readline

N ,L = map(int, input().split())
# 신호등의 정보 리스트의 인덱스는 신호등의 위치, 값은 신호등의 정보
imformation = [[]]  * (L + 1)

for _ in range(N):
    D, R, G = map(int, input().split())
    imformation[D] = [R, G]
# 상근이가 도로의 끝에 도착할 때까지 while문으로 상근이를 옮긴다.
sang = 0
time = 0
while sang < L:
    # 상근이가 신호등에 도착하면 신호에 맞게 기다리거나 출발한다.
    if imformation[sang] and time % (imformation[sang][0] + imformation[sang][1]) < imformation[sang][0]:
        time += 1
    else:
        sang += 1
        time += 1
            
print(time) 
    