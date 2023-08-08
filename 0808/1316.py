N = int(input())

cnt = 0
for i in range(N):
    # 그룹 단어면 True
    group = True
    word = input()

    # 단어의 글자 수
    len_word = 0
    for l in word:
        len_word += 1

    # 단어에서 바로 뒤가 연속되지 않으면 그 이후에는 연속된 글자가 없어야 한다.
    for i in range(len_word - 1):
        if word[i] != word[i + 1]:
            for j in range(i + 1, len_word):
                if word[i] == word[j]:
                    group = False
    
    if group == True:
        cnt += 1

print(cnt)