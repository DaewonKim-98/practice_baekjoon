import sys
input = sys.stdin.readline

string = str(input().strip())

# 대문자로
string = string.upper()

# 문자열 개수
len_str = 0
for i in string:
    len_str += 1

# 같은 수의 개수를 세고 딕셔너리로 만들고 최댓값을 찾는다.
max_cnt = 0
cnt_dic = {}
for i in range(len_str):
    cnt_dic[string[i]] = string.count(string[i])
    cnt = 0
    for j in range(i, len_str):
        if string[i] == string[j]:
            cnt += 1
    if max_cnt <= cnt:
        max_cnt = cnt

# 최댓값의 개수를 세고 key_list에 리스트 추가
nmax_cnt = 0
key_list = []
for k, v in cnt_dic.items():
    if v == max_cnt:
        nmax_cnt += 1
        key_list += [k]
    if nmax_cnt > 1:
        break
        
if nmax_cnt > 1:
    print('?')
else:
    print(key_list[0])