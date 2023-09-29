import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 수열 찾는 함수
def find(i):
    # M개가 되면 끝
    if i == M:
        print(' '.join(sequence))
        return
            
    else:
        for j in range(N):
                # 증가해야 하므로
                if i > 0:
                    if int(sequence[i - 1]) > arr[j]:
                        continue
                # 수열
                sequence[i] = str(arr[j])
                find(i + 1)
                        

N, M = map(int, input().split())
arr = list(range(1, N + 1))

visited = [0] * N
i = 0
sequence = [0] * M
find(i)