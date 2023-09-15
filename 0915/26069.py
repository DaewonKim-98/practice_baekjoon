import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
# 총총이 춤을 추는 사람을 set에 넣기
s = set(['ChongChong'])

for _ in range(N):
    a, b = map(str, input().split())
    # 세트에 있는 사람을 만나면 그 사람도 추가
    if a in s or b in s:
        s.add(a)
        s.add(b)


print(len(s))
