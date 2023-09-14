import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

S = list(input().strip())
q = int(input().strip())
l = len(S)
arr = [0] * l
dic = {}
for i in alpha:
    dic[i] = arr[::]
    # S를 돌면서 i와 같은 문자가 나오면 누적합으로 합에 추가
    if S[0] == i:
        dic[i][0] = 1
    for j in range(1, l):
        if S[j] == i:
            dic[i][j] = dic[i][j - 1] + 1
        else:
            dic[i][j] = dic[i][j - 1]


for i in range(q):
    a, l, r = map(str, input().split())
    l, r = int(l), int(r)
    # l이 0일때는 무조건 r에 따라서
    if l == 0:
        print(dic[a][r])
    # l일 때와 l -1일 때가 다르다면 l일때 늘어난 것이므로
    elif dic[a][l] > dic[a][l - 1]:
        print(dic[a][r] - dic[a][l] + 1)
    else:
        print(dic[a][r] - dic[a][l])

