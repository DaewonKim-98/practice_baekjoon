N = int(input())

# 중복조합 되려나
# 10HN이므로 (10 + N - 1)C9

result = 1
for i in range(9):
  result *= 10 + N - 1 - i
  result //= i + 1
  
result %= 10007
  
print(result)