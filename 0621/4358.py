import sys
input = sys.stdin.readline

dic = {}
cnt = 0
while True:
    tree = input().strip()
    if tree == '':
        break
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
    cnt += 1
    
lst = list(dic.keys())
lst.sort()
for name in lst:
    print(name, f"{((dic[name] / cnt) * 100):.4f}")