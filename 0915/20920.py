import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
# 단어와 단어의 개수를 나타내는 딕셔너리
dic = {}
for _ in range(N):
    word = input().rstrip()
    # 단어의 길이가 M이상인 것들만 ㄱㄱ
    if len(word) >= M:
        # word가 딕셔너리에 있으면 +1
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

# 딕셔너리를 리스트로
arr = []
for k, v in dic.items():
    arr.append([k, v])

# 리스트 정렬
# 처음은 알파벳 사전 순으로
arr.sort(key=lambda x: x[0])
# 다음은 해당 단어의 길이 순으로
arr.sort(key=lambda x: len(x[0]), reverse=True)
# 다음은 자주 나오는 단어 순으로
arr.sort(key=lambda x: x[1], reverse=True)

for w in arr:
    print(w[0])