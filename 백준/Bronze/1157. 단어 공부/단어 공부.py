string = input()
string = string.upper()
s = list(string)
s.sort()
count = 1
dic = {}
if len(s) == 1:
    print(s[0])
else:
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
            dic[s[i]] = count
        else:
            count = 1
            dic[s[i]] = count

    if list(dic.values()).count(max(dic.values())) > 1:
        print('?')
    else:
        print(max(dic, key=dic.get))