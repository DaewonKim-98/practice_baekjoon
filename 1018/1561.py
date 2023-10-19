N, M = map(int, input().split())
arr = list(map(int, input().split()))

if N <= M:
    print(N)

else:
    # N명의 놀이기구의 총 탑승 시간의 최소를 이분탐색으로
    start = 0
    end = max(arr) * N

    while start <= end:
        # 총 탑승 시간
        middle = (start + end) // 2

        # 아이
        kids = 0
        # 아이의 수는 총 탑승 시간에서 각각의 놀이기구를 나눈 몫과 같으므로
        for i in arr:
            kids += middle // i

        # 아이의 수가 N 보다 크면 총 탑승 시간의 길이를 줄여야하고
        if N - M <= kids:
            end = middle - 1
        # 아니면 총 탑승 시간의 길이를 늘려야 하므로
        else:
            start = middle + 1
        
    # 총 탑승 시간에서 각각의 놀이기구를 나눈 나머지가 0일 때 새로운 아이들이 탈 수 있으므로
    # 마지막에 타는 아이는 나머지가 0이면서 가장 뒤에 있는 것
    # print(start)
    # 총 탑승 시간 전까지 실제로 타고 내린 사람들은
    rided = 0
    for i in range(M):
        rided += start // arr[i]
        # 타고 있는 사람들도 추가
        if start % arr[i] != 0:
            rided += 1
    # 나머지 타야 하는 사람들은
    people = N - rided
    for i in range(M):
        if start % arr[i] == 0:
            people -= 1
            if people == 0:
                print(i + 1)
                break
