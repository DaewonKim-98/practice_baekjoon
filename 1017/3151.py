import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()

# 앞에서부터 가고 뒤에서부터 오는 투 포인터를 쓰면서 그 사이에 이분탐색?
cnt = 0
# j의 값에 따라서 딕셔너리 같은 것이 있을 때와 없을 때 따로 나눠서
j_dic_same = {}
j_dic_dif = {}
for i in range(arr):
    j_dic_same[i] = 0
    j_dic_dif[i] = 0
for j in range(N - 1, 1, -1):
    i = 0
    while i < j - 1:
        start = i + 1
        end = j - 1
        if arr[j] + arr[i] + arr[i + 1] > 0:
            break
        if arr[j] + arr[j - 1] + arr[i] < 0:
            i += 1
            continue
        while start <= end:
            middle = (start + end) // 2
            # print(i, j, middle)
            # 0이 된다면
            if arr[i] + arr[middle] + arr[j] == 0:
                if arr[middle] == arr[j]:
                    j_dic_same[middle] =
                cnt += 1
                # 똑같은 수가 있을 수 있으므로
                x = 1
                while middle + x < j:
                    if arr[i] + arr[middle + x] + arr[j] == 0:
                        cnt += 1
                        x += 1
                    else:
                        break

                y = 1
                while middle - y > i:
                    if arr[i] + arr[middle - y] + arr[j] == 0:
                        cnt += 1
                        y += 1
                    else:
                        break
                break
            
            elif arr[i] + arr[middle] + arr[j] < 0:
                start = middle + 1
            else:
                end = middle - 1

        i += 1

print(cnt)