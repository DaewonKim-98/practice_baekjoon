import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색을 할 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 꽃의 비용 리스트
prices = []

# 배열을 돌면서 비용 계산
for r in range(N):
    for c in range(N):
        # 초기 비용은 씨를 심은 곳
        price = arr[r][c]
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                 price += arr[nr][nc]
            else:
                break
        else:
            # 다음 꽃
            for r2 in range(N):
                for c2 in range(N):
                    # 꽃이 닿지 않게끔
                    if abs(r2 - r) + abs(c2 - c) >= 3:
                        # 초기 비용은 씨를 심은 곳
                        price2 = arr[r2][c2]
                        for d in dir:
                            nr, nc = r2 + d[0], c2 + d[1]
                            if 0 <= nr < N and 0 <= nc < N:
                                price2 += arr[nr][nc]
                            else:
                                break
                        else:
                            # 다음 꽃
                            for r3 in range(N):
                                for c3 in range(N):
                                    # 꽃이 닿지 않게끔
                                    if abs(r3 - r) + abs(c3 - c) >= 3 and abs(r3 - r2) + abs(c3 - c2) >= 3:
                                        # 초기 비용은 씨를 심은 곳
                                        price3 = arr[r3][c3]
                                        for d in dir:
                                            nr, nc = r3 + d[0], c3 + d[1]
                                            if 0 <= nr < N and 0 <= nc < N:
                                                price3 += arr[nr][nc]
                                            else:
                                                break
                                        else:

                                            prices.append(price + price2 + price3)
                            

print(min(prices))