N = int(input())
arr = [int(input()) for _ in range(N)]

# 정렬한 다음에 등수도 1번부터 차례로 만들어 그 차들의 합을 구한게
# 최소가 되는 건가?? 안되면 컴퓨터 부순다.

arr.sort()
rank = list(range(1, N + 1))

angry = 0
for i in range(N):
    angry += abs(arr[i] - rank[i])
    
print(angry)