import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 동, 은, 금 순으로 정렬
arr.sort(key=lambda x: x[3], reverse=True)
arr.sort(key=lambda x: x[2], reverse=True)
arr.sort(key=lambda x: x[1], reverse=True)
for i in range(N):
    # K 나라에 도달하면
    if arr[i][0] == K:
        # i가 0이면 가장 높은 나라라는 것이므로 1등
        if i == 0:
            print(1)
            break
        else:
            # K 나라 앞으로 탐색해서 자신과 메달이 다른 나라를 탐색해서 다른 나라의 인덱스 + 2 출력
            for j in range(i - 1, -1, -1):
                if arr[j][1] != arr[i][1] or arr[j][2] != arr[i][2] or arr[j][3] != arr[i][3]:
                    print(j + 2)
                    break
            # break이 안되고 0까지 갔으면 공동 1위라는 의미이므로
            else:
                print(1)
                break