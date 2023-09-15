import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
# 곰곰티콘을 쓴 아이디 목록
s = set()
cnt = 0

for _ in range(N):
    record = str(input().strip())
    # ENTER가 나오면 arr 다시 빈 리스트로 만들어주기
    if record == 'ENTER':
        s = set()
    # 다른 문자가 나왔을 때 처음 나온 것이면 set에 추가하고 곰곰티콘 카운트
    elif record not in s:
        cnt += 1
        s.add(record)
    # 아니면 필요 없으므로
    else:
        pass

print(cnt)
