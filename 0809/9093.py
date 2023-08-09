T = int(input())

for case in range(1, T + 1):
    sen = list(map(str, input().split()))

    # sentence에서 word를 반복을 돌려서 거꾸로 만들고 다시 nsen에 추가
    nsen = []
    for word in sen:
        nword = ''
        for i in range(len(word) - 1, -1, -1):
            nword += word[i]
        nsen += [nword]

    # 뒤바뀐 단어들을 출력
    for j in nsen:
        print(j, end=' ')
    print()