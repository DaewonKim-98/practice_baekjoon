import sys
input = sys.stdin.readline

T = int(input().strip())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    # 간선 리스트
    e_list = [list(map(int, input().split())) for _ in range(M)]

    # 비행기 종류의 최소 개수는 연결된 간선의 개수이므로 N - 1
    print(N - 1)