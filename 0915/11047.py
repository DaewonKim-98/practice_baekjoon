import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input().strip()) for _ in range(N)]

# 뒤에서부터 arr을 읽으면서 동전을 나누고 카운트
cnt = 0
while K > 0:
    for i in range(N - 1, - 1, -1):
        # 나누었을 때 몫이 0보다 크면 나눌 수 있다는 것이므로
        if K // arr[i] > 0:
            cnt += 1
            K = K - arr[i]
            break

print(cnt)
