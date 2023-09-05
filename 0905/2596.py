import sys
input = sys.stdin.readline

dic = {
    '000000':'A',
    '001111':'B',
    '010011':'C',
    '011100':'D',
    '100110':'E',
    '101001':'F',
    '110101':'G',
    '111010':'H'    
}

N = int(input().strip())
word = input().strip()
# 6개씩 돌아가면서 읽고 문자가 맞는지 확인 후 출력
understand_word = ''
result = 0
for i in range(0, N * 6, 6):
    cnt_list = []
    for k, v in dic.items():
        # 똑같은 숫자면 카운트
        cnt = 0
        for j in range(6):
            if k[j] == word[i + j]:
                cnt += 1
        # 카운트가 6이 된다면 understand_word 넣고 종료
        if cnt == 6 or cnt == 5:
            understand_word += v
            break
    # break이 안된다면 모두 돌아간 것이고 그것은 찾을 수 없다는 뜻이므로
    else:
        result = i // 6 + 1
        break

# result가 0이면 모두 정상적으로 돌아갔으므로
if result == 0:
    print(understand_word)
else:
    print(result)

