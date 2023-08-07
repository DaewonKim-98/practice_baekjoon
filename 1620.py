import sys

N, M = map(int, input().split())

# 포켓몬과 그 순서 딕셔너리를 만든다
pocketmon = {}
pocketmon_num = {}
for i in range(N):
    v = str(sys.stdin.readline().strip())
    pocketmon[v] = i + 1
    pocketmon_num[i + 1] = v
    
# 들어오는 값 정수로 바뀌면 정수 딕셔너리에서 출력, 아니면 포켓몬에서 출력
for j in range(M):
    word = sys.stdin.readline().strip()
    if word.isdigit():
        word = int(word)
        print(pocketmon_num[word])
    else:
        print(pocketmon[word])