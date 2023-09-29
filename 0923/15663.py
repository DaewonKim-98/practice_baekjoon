import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# M개의 수열을 찾는 함수
def find(i):
    if i == M:
        # if sequence not in sequence_list:
            sequence_list.append(sequence[:])
            return
    else:
        for j in range(N):
            # 방문하지 않았으면
            if visited[j] == 0:
                # 수열에 추가
                sequence[i] = str(arr[j])
                # 만약 사용했던 수열이라면 또 쓰는 것은 중복이므로
                if tuple(sequence) in used:
                    # 다시 0으로
                    sequence[i] = 0
                    continue
                used.add(tuple(sequence[:]))
                # 방문 표시
                visited[j] = 1
                # 재귀
                find(i + 1)
                visited[j] = 0
                # 다시 0으로
                sequence[i] = 0
    
    
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N
sequence = [0] * M
i = 0
sequence_list = []
# 사용했던 모든 리스트들 집합
used = set()
find(i)
# print(used)
for s in sequence_list:
    print(' '.join(s))
