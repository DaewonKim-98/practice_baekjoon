A, B = map(int, input().split())
cnt = 1

# B가 0이되면 끝이므로
while True:
    if A == B:
        break
    elif B <= 1:
        cnt = -1
        break
    # 가장 뒤에 1이 있으면 빼주기
    elif str(B)[-1] == '1':
        B = int(str(B)[:-1])
        cnt += 1
    # 2 나눠주기
    else:
        if B % 2 == 0:
            B //= 2
            cnt += 1
        else:
            cnt = -1
            break
   
print(cnt)