def change(i):
    if arr[i] == '0':
        arr[i] = '1'
    else:
        arr[i] = '0'
        
def change_copy(i):
    if arr_copy[i] == '0':
        arr_copy[i] = '1'
    else:
        arr_copy[i] = '0'

N = int(input())
arr = list(input())
will_make = list(input())

# 똑같으면 바꿀 필요가 없으므로
if arr == will_make:
    print(0)
    exit()
cnt = 0

# 처음이 문젠데 처음을 누르고 안누르고 생각해서 따로 생각해주면 되려나 아오
# i번째를 누르면 무조건 i - 1번째가 바뀌니까 이자식이 다르면 i번째 다르게
arr_copy = arr[:]

# 처음을 안눌렀을 때
for i in range(1, N):
    if arr_copy[i - 1] != will_make[i - 1]:
        cnt += 1
        change_copy(i - 1)
        change_copy(i)
        if i != N - 1:
            change_copy(i + 1)
# 다 바꿨을 때 답이랑 같으면 cnt 출력 오 지렸다 이거네
if arr_copy == will_make:
    print(cnt)
    exit()
    
# 처음을 누르고 시작하면
cnt = 1
change(0)
change(1)

for i in range(1, N):
    if arr[i - 1] != will_make[i - 1]:
        cnt += 1
        change(i - 1)
        change(i)
        if i != N - 1:
            change(i + 1)
# 다 바꿨을 때 답이랑 같으면 cnt 출력 오 지렸다 이거네
if arr == will_make:
    print(cnt)
    exit()
    
# 안끝났으면 다르므로
print(-1)