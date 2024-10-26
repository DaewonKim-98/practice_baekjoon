N = int(input())
arr = list(map(int, input().split()))

maxCnt = 0
i = 0
j = 0
kind_count = {}

while j < N:
    # 과일 종류의 개수를 추가
    if arr[j] in kind_count:
        kind_count[arr[j]] += 1
    else:
        kind_count[arr[j]] = 1
    
    # 과일 종류가 2를 초과하면 i 포인터를 이동
    while len(kind_count) > 2:
        kind_count[arr[i]] -= 1
        if kind_count[arr[i]] == 0:
            del kind_count[arr[i]]
        i += 1
    
    # 최대 길이 갱신
    maxCnt = max(maxCnt, j - i + 1)
    j += 1

print(maxCnt)
