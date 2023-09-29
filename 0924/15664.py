import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 수열 찾는 함수
def find(i):
    # M개가 되면 끝
    if i == M:
        if sequence not in sequence_list:
            sequence_list.append(sequence[:])
        return
            
    else:
        duplication = 0
        for j in range(N):
             # 방문하지 않았으면
             if visited[j] == 0:
                # 중복된게 아니면
                if duplication != arr[j]:
                    # 증가하는 수열이여야 하므로
                    if i > 0:
                        if int(sequence[i - 1]) <= arr[j]:
                            # 중복 표시
                            duplication = arr[j]
                            # 방문 표시
                            visited[j] = 1
                            # 수열
                            sequence[i] = str(arr[j])
                            find(i + 1)
                            # 다시 방문 제거
                            visited[j] = 0
                    else:
                        # 중복 표시
                        duplication = arr[j]
                        # 방문 표시
                        visited[j] = 1
                        # 수열
                        sequence[i] = str(arr[j])
                        find(i + 1)
                        # 다시 방문 제거
                        visited[j] = 0
                        

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N
i = 0
sequence = [0] * M
sequence_list = []
find(i)
for s in sequence_list:
    print(' '.join(s))