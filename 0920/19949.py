import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(i, score):
    # print(j_list, i, score)
    global cnt
    # 10문제까지 다 돌면 끝
    if i == 10:
        # 점수가 5점 이상이면 카운트
        if score >= 5:
            cnt += 1
        return
    elif i < 2:
        # 문제 문항
        for j in range(1, 6):
            j_list[i] = j
            # 찍은 문제와 답이 같으면 score + 1
            if j == arr[i]:
                dfs(i + 1, score + 1)
                j_list[i] = 0
            # 아니면 그대로 i만 + 1
            else:
                dfs(i + 1, score)
                j_list[i] = 0
    # i가 2 이상이면 연속이 나오므로
    elif i >= 2:
        for j in range(1, 6):
            j_list[i] = j
            # 3문제 모두 연속이면 필요 없으므로
            if j_list[i - 2] == j_list[i - 1] == j_list[i]:
                j_list[i] = 0
                continue
            elif j == arr[i]:
                dfs(i + 1, score + 1)
                j_list[i] = 0
            else:
                dfs(i + 1, score)
                j_list[i] = 0


arr = list(map(int, input().split()))

score = 0
i = 0
# 경우의 수
cnt = 0
# 찍은 문제 리스트
j_list = [0] * 10
dfs(i, score)
print(cnt)