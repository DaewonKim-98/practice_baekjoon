N = int(input())

# 2차원 배열을 만든다.
arr = []
for i in range(N):
    arr.append(list(input()))

nfile = ''
# 열 우선 탐색으로 같으면 그대로 출력하고 다른 것이 있으면 ?로 출력
for c in range(len(arr[0])):
    # set으로 모두 같은지 아니면 다른 것이 있는지 판단
    same = set()
    for r in range(N):
        word = arr[r][c]
        same.add(word)
    
    # 세트의 길이가 1이라는 것은 모두 같다는 것이므로
    if len(same) == 1:
        nfile += word
    # 아니면 ?를 더한다.
    else:
        nfile += '?'

print(nfile)

    