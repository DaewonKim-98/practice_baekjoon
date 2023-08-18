N = int(input())

arr = list(range(1, N + 1))

# 버린 카드를 출력하고 남는 카드도 마지막에 버리고 출력
while len(arr) > 0:
    print(arr.pop(0), end=' ')
    if len(arr) == 0:
        break
    arr.append(arr.pop(0))
    