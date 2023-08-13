import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque(list(map(int, input().split())))

# 처음 풍선을 터뜨리고 풍선의 번호 리스트와 새로 나열되는 풍선 번호리스트를 만든다.
balloon = arr.popleft()
num_list = deque(list(range(1, N + 1)))
num = num_list.popleft()
# 처음에는 1이 들어간다.
balloon_list = deque([num])

# balloon_list가 다 찰 때까지 반복
while len(balloon_list) < N:
    # 터진 풍선이 양수일 때는 앞에 balloon - 1개를 뒤로 옮긴다.
    if balloon > 0:
        for i in range(balloon - 1):
            arr.append(arr.popleft())
            # 번호리스트도 마찬가지로 앞에 balloon - 1개를 뒤로 옮긴다.
            num_list.append(num_list.popleft())
    # 터진 풍선이 음수일 때는 뒤에 balloon 개를 앞으로 옮긴다.
    # balloon이 음수이므로 -를 붙임
    else:
        for i in range(-balloon):
            arr.appendleft(arr.pop())
            # 번호리스트도 마찬가지로 뒤에 balloon 개를 앞으로 옮긴다.
            num_list.appendleft(num_list.pop())
            
    # 이제 가장 앞에 있는 풍선이 다음 터뜨릴 풍선이 되므로
    balloon = arr.popleft()
    # 번호도 가장 앞에 있는 번호이므로 새 풍선 번호 리스트에 추가
    balloon_list.append(num_list.popleft()) 
    
for i in balloon_list:
    print(i, end=' ')
    
