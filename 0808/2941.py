# 크로아티아 문자들에서 2글자와 3글자를 나눈다.
croatia2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
croatia3 = ['dz=']

string = input().strip()

# string의 문자열 수를 센다.
len_str = 0
for i in string:
    len_str += 1


cnt = 0
# 문자열에서 2글자짜리 크로아티아 문자가 있으면 전체 문자열 크기에서 -1
for word in croatia2:
    for s in range(len_str - 1):
        if string[s] + string[s + 1] == word:
            cnt += 1

# 문자열에서 3글자짜리 크로아티아 문자가 있으면 전체 문자열 크기에서 -1: 
# dz= 에는 z=도 포함되어위에서 또 - 되기 때문에 1만 빼준다.
for word in croatia3:
    for s in range(len_str - 2):
        if string[s] + string[s + 1] + string[s + 2] == word:
            cnt += 1

print(len_str - cnt)