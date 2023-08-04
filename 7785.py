N = int(input())

arr = []
for i in range(N):
    lst = list(map(str, input().split()))
    arr.append(lst)

# 이름과 출결 기록을 딕셔너리의 키와 값으로 받는다.(중복된 키는 덮어짐)
dic = {}
for j in range(N):
    dic[arr[j][0]] = arr[j][1]

# 키에서 'leave'가 있으면 제거
for k in list(dic.keys()):
    if dic[k] == 'leave':
        dic.pop(k)

# 키만 리스트로 받아서 역순으로 정렬
names = list(dic.keys())
names.sort(reverse=True)

# 출력
for name in names:
    print(name)