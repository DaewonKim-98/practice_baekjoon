import sys
from itertools import combinations as c
input = sys.stdin.readline

N = int(input().strip())
number = list(range(N))
arr = [list(map(int, input().split())) for _ in range(N)]

result = 1000000
# 조합을 사용해서 스타트팀과 링크팀 구별
for start in c(number, N//2):
    sum_start, sum_link = 0, 0
    # 링크팀은 세트에서 전체에서 스타트 팀 뺀 것
    link = list(set(number) - set(start))
    # 마찬가지로 세트팀에서 조합으로 2개를 고르고 스타트에 플러스
    for r in c(start, 2):
        sum_start += arr[r[0]][r[1]]
        sum_start += arr[r[1]][r[0]]

    for r in c(link, 2):
        sum_link += arr[r[0]][r[1]]
        sum_link += arr[r[1]][r[0]]
    result = min(result, abs(sum_start-sum_link))
print(result)