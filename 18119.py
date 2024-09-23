import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 각 단어가 사용하는 알파벳 집합을 저장
word_sets = []
for _ in range(N):
    word = set(input().strip())
    word_sets.append(word)

# 현재 알고 있는 알파벳을 저장
known_spells = set(chr(i) for i in range(ord('a'), ord('z')+1))

# 쿼리 처리
for _ in range(M):
    o, x = input().strip().split()

    if o == '1':  # 스펠링 삭제
        known_spells.discard(x)
    else:         # 스펠링 추가
        known_spells.add(x)

    # 현재 알고 있는 스펠링으로 알 수 있는 단어의 수를 계산
    count = 0
    for word in word_sets:
        if word.issubset(known_spells):
            count += 1

    print(count)
