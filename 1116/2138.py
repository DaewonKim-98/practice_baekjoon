def change(a):
    if a == '0':
        a = '1'
    else:
        a = '0'

N = int(input())
arr = list(input())
will_make = list(input())

# 똑같으면 바꿀 필요가 없으므로
if arr == will_make:
    print(0)
    exit()
cnt = 0
# N이 2일 때 하나의 스위치로 둘 다 바뀌므로 -1 출력
if N == 2:
    print(-1)
    exit()

