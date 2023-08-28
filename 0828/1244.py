import sys
input = sys.stdin.readline

N = int(input().strip())
switch = list(map(int, input().split()))
M = int(input().strip())
# 들어오는 학생의 성별에 맞게 스위치를 변환
for i in range(M):
    g, s = map(int, input().split())
    # 남자라면 s의 배수만큼 스위치 변환
    if g == 1:
        # s의 배수가 N보다 같거나 클 때까지 반복
        sb = s
        while sb <= N:
            # s는 자연수이므로 인덱스로 바꾸러면 1 마이너스
            if switch[sb - 1] == 0:
                switch[sb - 1] = 1
            else:
                switch[sb - 1] = 0
            # s의 배수는 계속 s를 더한 것
            sb += s
    # 여자라면 s의 양 옆이 대칭이면 그만큼 스위치 변환
    else:
        # 처음에는 최대로 시작
        symmetry = 0
        # 대칭의 최대는 symmetry 까지이므로
        for j in range(N // 2 + 2):
            # 범위 내에서
            if s - 1 - j >= 0 and s - 1 + j <= N - 1:
                # 다른 부분이 나오면 바로 끝
                if switch[s - 1 + j] != switch[s - 1 - j]:
                    break
                symmetry = j
        # symmetry 전까지가 대칭이므로
        for k in range(s - 1 - symmetry, s - 1 + symmetry + 1):
            if 0 <= k < N:
                if switch[k] == 0:
                    switch[k] = 1
                else:
                    switch[k] = 0

for i in range((N + 19) // 20):
    if 20 * i < N <= 20 * (i + 1):
        print(*switch[20 * i:])
    else:
        print(*switch[20 * i:20 * (i + 1)])