D, K = map(int, input().split())

# a b a+b a+2b 2a+3b 3a+5b 5a+8b
# 피보나치수열
fibo = [1] + [1] + [0] * 28
for i in range(2, 30):
  fibo[i] = fibo[i - 1] + fibo[i - 2]

# 떡의 개수는 K = A * fibo[D - 3] + B * fibo[D - 2]
for i in range(1, 50001):
  for j in range(1, 50001):
    if i * fibo[D - 3] + j * fibo[D - 2] == K:
      print(i)
      print(j)
      exit()