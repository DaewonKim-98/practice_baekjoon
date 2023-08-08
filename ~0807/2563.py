N = int(input())

# 정사각형 N개의 넓이를 먼저 구해준다.
area = 100 * N

# papers를 가로 세로의 크기가 100인 정사각형으로 만든다
papers = []
for i in range(100):
    papers += [[0] * 100]
# N 개의 정사각형을 반복한다
for cnt in range(N):
    # 순서대로 x, y 좌표 리스트를 뽑고
    paper = list(map(int, input().split()))
    # 좌표 리스트에서 정사각형에 해당하는 부분들을 1로 둔다.
    for num1 in range(-1, 9):
        for num2 in range(-1, 9):
            papers[paper[1] + num1][paper[0] + num2] = 1

# 1의 값들을 세면 그것들이 검은 영역의 넓이
count = 0
for i in papers:
    count += i.count(1)
print(count)