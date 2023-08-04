N = int(input())

arr = []
for i in range(N):
    lst = list(map(str, input().split()))
    arr.append(lst)

dic = {}
for j in range(N):
    dic[arr[j][0]] = arr[j][1]

for k in list(dic.keys()):
    if dic[k] == 'leave':
        dic.pop(k)

names = list(dic.keys())
names.sort(reverse=True)

for name in names:
    print(name)