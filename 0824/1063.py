import sys

# 열을 숫자로 변환
dic = {}
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num = list(range(8))
for i in range(8):
    dic[alpha[i]] = num[i]

king, rock, N = map(str, input().split())
# 킹과 돌의 위치를 배열의 인덱스화
[c1, r1] = list(king)
c1 = int(dic[c1])
r1 = 8 - int(r1)

[c2, r2] = list(rock)
c2 = int(dic[c2])
r2 = 8 - int(r2)

# 명령대로 수행
for _ in range(int(N)):
    commend = input().strip()
    if commend == 'R':
        if c1 + 1 < 8:
            c1 += 1
        # 돌과 같은 곳으로 이동할 때 돌을 움직인다.
        if c1 == c2 and r1 == r2:
            # 돌이 밖으로 나가면 안되므로
            if c2 + 1 < 8:
                c2 += 1
            # 돌이 밖으로 나가면 킹도 다시 원위치
            else:
                c1 -= 1
    elif commend == 'L':
        if c1 - 1 >= 0:
            c1 -= 1
        if c1 == c2 and r1 == r2:
            if c2 - 1 >= 0:
                c2 -= 1
            else:
                c1 += 1
    elif commend == 'B':
        if r1 + 1 < 8:
            r1 += 1
        if c1 == c2 and r1 == r2:
            if r2 + 1 < 8:
                r2 += 1
            else:
                r1 -= 1
    elif commend == 'T':
        if r1 - 1 >= 0:
            r1 -= 1
        if c1 == c2 and r1 == r2:
            if r1 - 1 >= 0:
                r2 -= 1
            else:
                r1 += 1
    elif commend == 'RT':
        if r1 - 1 >= 0 and c1 + 1 < 8:
            r1 -= 1
            c1 += 1
        if c1 == c2 and r1 == r2:
            if r1 - 1 >= 0 and c1 + 1 < 8:
                r2 -= 1
                c2 += 1
            else:
                r1 += 1
                c1 -= 1
    elif commend == 'LT':
        if r1 - 1 >= 0 and c1 - 1 >= 0:
            r1 -= 1
            c1 -= 1
        if c1 == c2 and r1 == r2:
            if r1 - 1 >= 0 and c1 - 1 >= 0:
                r2 -= 1
                c2 -= 1
            else:
                r1 += 1
                c1 += 1
    elif commend == 'RB':
        if r1 + 1 < 8 and c1 + 1 < 8:
            r1 += 1
            c1 += 1
        if c1 == c2 and r1 == r2:
            if r1 + 1 < 8 and c1 + 1 < 8:
                r2 += 1
                c2 += 1
            else:
                r1 -= 1
                c1 -= 1
    elif commend == 'LB':
        if r1 + 1 < 8 and c1 - 1 >= 0:
            r1 += 1
            c1 -= 1
        if c1 == c2 and r1 == r2:
            if r1 + 1 < 8 and c1 - 1 >= 0:
                r2 += 1
                c2 -= 1
            else:
                r1 -= 1
                c1 += 1
                
# 다시 문제대로 변환
king = str(alpha[c1]) + str(8 - r1)
rock = str(alpha[c2]) + str(8 - r2)

print(king)
print(rock)