import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
road = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 주유소 가격의 최솟값을 구하는데 마지막 주유소는 제외
last = prices.pop()
min_idx = prices.index(min(prices))

# 최소 비용은 가면서 주유소 가격이 자기보다 작으면 계속 그 주유소에서 충전1
price = 0
cnt = 0
# 인덱스 i와 주유한 위치
i = 0
place = 0
while i < N - 1:
    # 만약 주유한 위치보다 i일 때가 가격이 더 싸면 place 갱신
    if prices[place] > prices[i]:
        place = i 
    # 최소의 주유소 가격을 가진 주유소에 도착하면
    if i == min_idx:
        place = min_idx
    # 주유하는 가격은
    price += road[i] * prices[place]
    i += 1
    
        
print(price)