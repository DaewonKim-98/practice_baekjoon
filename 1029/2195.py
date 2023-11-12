S = input()
P = input()

# P를 돌면서 문자열이 S에 있는지 찾고 있으면 cnt 늘리기 없으면 이전 것으로
i = 0
string = ''
cnt = 0
while i < len(P):
    if len(string) == 0:
        string += P[i]
        i += 1
    else:
        if string in S:
            string += P[i]
            i += 1
        else:
            string = ''
            i -= 1
            cnt += 1
            
# 다 돌았을 때 string이 있으면
if len(string) == 1:
    cnt += 1
else:
    if string in S:
        cnt += 1
    else:
        cnt += 2
        
print(cnt)