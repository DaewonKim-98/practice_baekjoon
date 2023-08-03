N = int(input())
arr = list(map(int, input().split()))

# 처치할 수 있는 최대 숫자를 best_kill로 둔다.
best_kill = 0
for idx in range(N - 1):
    if best_kill >= N - idx:
        break
    # 각각의 봉우리에서 처치할 수 있는 숫자를 kill로 둔다.
    kill = 0
    for nidx in range(idx + 1, N):
        # 만약 각각의 봉우리보다 다음의 봉우리가 작으면 kill에 1을 더한다.
        if arr[idx] > arr[nidx]:
            kill += 1
            # 처치할 수 있는 최대 숫자를 자신보다 더 큰 kill로 갱신
            if best_kill < kill:
                best_kill = kill
        # 아니면 break
        else:
            break


print(best_kill)