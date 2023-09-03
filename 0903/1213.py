import sys
input = sys.stdin.readline

name = list(input().strip())
name.sort()
copy_name = name[::]

result = 0
# 홀수면 카운트
cnt_odd = 0
pel = ''
# 이름을 돌면서 각 알파벳의 개수 구하기
for i in copy_name:
    # 알파벳의 개수가 홀수면 카운트
    if name.count(i) % 2 == 1:
        cnt_odd += 1
        # 펠린드롬에 홀수 추가
        pel += i
        name.remove(i)
        
    # 만약 홀수인 것이 2개 이상이면 팰린드롬이 안되므로
    if cnt_odd > 1:
        break

if cnt_odd > 1:
    print("I'm Sorry Hansoo")
    
else:
    # 전체를 돌면서 팰린드롬 만들어주기
    left = ''
    for j in range(0, len(name), 2):
        left += name[j]
    right = left[::-1]
        
    print(left + pel + right)