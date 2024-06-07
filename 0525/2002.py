N = int(input())
entrance = [input() for _ in range(N)]
exit = [input() for _ in range(N)]

# 입구와 출구 인덱스를 따로 두고 같으면 넘어가고 다르면 출구 +1
cnt = 0
i = 0
j = 0
overtaking = set()
while j < N:
    if entrance[i] == exit[j]:
        i += 1
        j += 1
    elif entrance[i] in overtaking:
        i += 1
    else:
        overtaking.add(exit[j])
        cnt += 1
        j += 1
    # print(i, j, cnt)
print(cnt)