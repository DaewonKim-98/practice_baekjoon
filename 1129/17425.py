import sys
input = sys.stdin.readline

N = int(input().strip())

# 트리 정보를 담을 세트
info_set = set()
for _ in range(N):
    arr = list(map(str, input().strip().split()))
    K = int(arr[0])
    # 트리 정보를 앞에서부터 쭉 연결해서 세트에 담기
    info = []
    for i in range(K):
        # info += arr[i + 1]
        info.extend([arr[i + 1]])
        info_set.add(tuple(info))

# 정보들을 리스트로 만든 뒤 정렬     
info_set = list(info_set)
info_set.sort()

# print(info_set)

# 순서에 맞게 출력
for i in range(len(info_set[0])):
    result = '--' * i + info_set[0][i]
    print(result)
for i in range(1, len(info_set)):
    for j in range(len(info_set[i])):
        # 만약 자신 앞에 있는 굴을 자신이 가지고 있으면 출력 안해도 되므로
        if j < len(info_set[i - 1]) and info_set[i][j] == info_set[i - 1][j]:
            pass
        else:
            result = '--' * j + info_set[i][j]
            print(result)
        