N = int(input())

lst = []
count = 0
dic = {}

# 1 부터 시작해서 충분히 큰 수까지 666이 들어간 것들을
# 처음부터 세서 딕셔너리에 넣고 나중에 그 순서에 맞는 것 출력
for i in range(1, 10000000):
    if '666' in str(i):
        count += 1
        dic[count] = i
    else:
        pass

print(dic[N])
