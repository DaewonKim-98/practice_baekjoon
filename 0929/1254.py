arr = list(input())

# 다시 처음부터 시작해보자.
# 가장 뒤에 수와 같은 수를 찾고 그자식이랑 그 사이가 팰린드롬이면 그 전까지를
# +해서 출력, 없으면 전체 문자열을 더해서 출력
pel = False
last = len(arr) - 1
idx = 0
for i in range(last):
    if arr[i] == arr[last]:
        start = i
        idx = i
        # start와 last가 만날 때까지 while문 반복
        while start <= last:
            if arr[start] == arr[last]:
                start += 1
                last -= 1
                pel = True
            else:
                pel = False
                last = len(arr) - 1
                break
        # while문이 끝났을 때 pel = True면 바로 끝
        if pel == True:
            break

if pel == True:
    print(len(arr) + idx)
    
else:
    print(len(arr) * 2 - 1)