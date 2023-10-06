arr = []

while True:
    try:
        arr.append(int(input()))

    except:
        break

# 트리 나누기 처음은 루트와 끝
def postorder(start, end):
    # 왼쪽이 오른쪽보다 커진다면 return
    if start > end:
        return
    
    # 루트 노드가 가장 클 때, 오른쪽이 없을 때를 대비해
    mid = end + 1
    # start 다음부터 시작해 end까지 갈 때 큰 값이 나오면 오른쪽 값이므로
    for i in range(start + 1, end + 1):
        if arr[i] > arr[start]:
            mid = i
            break
    
    # print(start, mid, end)
    # 왼쪽으로 가서 반복
    postorder(start + 1, mid - 1)
    # 오른쪽으로 가서 반복
    postorder(mid, end)
    print(arr[start])

postorder(0, len(arr) - 1)