import sys
input = sys.stdin.readline

T = int(input().strip())
for case in range(1, T + 1):
  N, K, ID, M = map(int, input().strip().split())
  # 각 팀에 대해 마지막 제출 시간과 문제의 점수를 나타내는 리스트를 리스트로
  arr = [0] * N
  for i in range(N):
    arr[i] = [i, 0, 0, [0] * (K + 1)]
  # 시간, 점수 저장
  for time in range(M):
    i, j, s = map(int, input().strip().split())
    arr[i - 1][1] = time
    arr[i - 1][2] += 1
    arr[i - 1][3][j] = max(s, arr[i - 1][3][j])
  # 최종 점수, 문제 풀이 횟수, 시간에 따라 정렬
  # arr.sort(key=lambda x: x[1])
  # arr.sort(key=lambda x: x[2])
  arr.sort(key=lambda x: (-sum(x[3]), x[2], x[1]))
  
  for i in range(N):
    if arr[i][0] == ID - 1:
      print(i + 1)
      break