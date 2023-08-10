N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

# 간격 리스트를 만든다.
sub_list = []
for i in range(len(arr) - 1):
    sub_list.append(arr[i + 1] - arr[i])

# 간격들의 최대 공약수가 가로수를 가장 적게 심을 수 있는 간격
gcd = sub_list[0]
# 간격들의 최대 공약수를 찾는다.
for i in range(len(sub_list) - 1):
    # 유클리드 호제법
    while sub_list[i + 1] != 0:
        [gcd, sub_list[i + 1]] = [sub_list[i + 1], gcd % sub_list[i + 1]]
        
# 가로수의 수는 간격에 따라 다르므로 가장 뒤와 가장 앞의 수를 간격으로 나눈 몫의 차
print(arr[-1] // gcd - arr[0] // gcd + 1 - len(arr))