import sys

N = int(sys.stdin.readline())

# 10000개 이하의 수가 주어지므로 처음 인덱스를 제외하고 셀 10001개의 0 리스트
arr = [0]*10001
# 리스트의 인덱스의 값에 1을 더해주므로써 들어온 값이 인덱스가 되고
# 그 값은 들어온 값의 개수를 나타낸다.
for i in range(N):
    data = int(sys.stdin.readline())
    arr[data] += 1

for j in range(10001):
    # 값이 0인 부분은 들어온 값이 없다는 뜻이므로 빼고
    if arr[j] != 0:
        # 개수만큼 j를 출력해주면 오름차순으로 정렬된다.
        for k in range(arr[j]):  
            print(j)