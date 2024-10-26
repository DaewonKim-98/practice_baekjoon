rtn = {
  'I':1,
  "V":5,
  'X':10,
  'L':50,
  'C':100,
  'D':500,
  'M':1000
}

A = list(input())
B = list(input())

# 작은 숫자가 앞에 오면 빼기, 나머지는 걍 더하기
i = 0
numA = 0
while i < len(A):
  if i + 1 < len(A) and rtn[A[i]] < rtn[A[i + 1]]:
    numA += rtn[A[i + 1]] - rtn[A[i]]
    i += 2
  else:
    numA += rtn[A[i]]
    i += 1
i = 0
numB = 0
while i < len(B):
  if i + 1 < len(B) and rtn[B[i]] < rtn[B[i + 1]]:
    numB += rtn[B[i + 1]] - rtn[B[i]]
    i += 2
  else:
    numB += rtn[B[i]]
    i += 1

result = numA + numB
print(result)

ara = str(result)
result = ''
while len(ara) < 4:
  ara = '0' + ara

result += int(ara[0]) * 'M'
if int(ara[1]) >= 5:
  if int(ara[1]) == 9:
    result += 'CM'
  else:
    result += 'D'
    result += (int(ara[1]) - 5) * 'C'
elif int(ara[1]) < 5:
  if int(ara[1]) == 4:
    result += 'CD'
  else:
    result += int(ara[1]) * 'C'
if int(ara[2]) >= 5:
  if int(ara[2]) == 9:
    result += 'XC'
  else:
    result += 'L'
    result += (int(ara[2]) - 5) * 'X'
elif int(ara[2]) < 5:
  if int(ara[2]) == 4:
    result += 'XL'
  else:
    result += int(ara[2]) * 'X'
if int(ara[3]) >= 5:
  if int(ara[3]) == 9:
    result += 'IX'
  else:
    result += 'V'
    result += (int(ara[3]) - 5) * 'I'
elif int(ara[3]) < 5:
  if int(ara[3]) == 4:
    result += 'IV'
  else:
    result += int(ara[3]) * 'I'
print(result)