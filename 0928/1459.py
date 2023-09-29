X, Y, W, S = map(int, input().split())

# 두 블록 가는데 걸리는 시간이 대각선보다 짧으면 대각선을 이용 안하는게 나으므로
if 2 * W <= S:
    print((X + Y) * W)

# 이외에 대각선이 한 블록 가는 것보다는 시간이 길면 대각선을 다 이용한 다음
# 블록을 이용하는게 나으므로
elif W <= S:
    print(min(X, Y) * S + (max(X, Y) - min(X, Y)) * W)

# 대각선이 한 블록 가는 것보다 짧으면 대각선만 이용하는게 나으므로
else:
    # 높은 것과 낮은 것의 차가 짝수이면
    if (max(X, Y) - min(X, Y)) % 2 == 0:
        print(max(X, Y) * S)
    # 홀수이면 마지막에 블록을 하나 이용
    else:
        print((max(X, Y) - 1) * S + W)