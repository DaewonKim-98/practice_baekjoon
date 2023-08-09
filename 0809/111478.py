import sys

string = str(sys.stdin.readline().strip())

# i만큼 j부터 시작해서 연속된 문자들을 string_lst에 넣는다.
string_lst = []
for i in range(1, len(string) + 1):
    for j in range(len(string) - i + 1):
        string_lst.append(string[j:j+i])

# 중복 제거
string_lst = set(string_lst)
print(len(string_lst))