A, B = map(int, input().split())
# 다시다시다시다시닷디ㅏ시닷디ㅏㅅ디ㅏㅅ디ㅏ다ㅣ시다시다시다시!!!!!!!!!!!!!11
# 그냥 360으로 나누어 떨어지는 것이 아니면 파이썬이라 소수 계산에서 에러 나는듯
# 결국은 다시 해서 소수를 찾고 자신보다 작은 소수로 자기가 나누어 떨어지면
# 그 몫을 빼주면 된다

sosu = set()
for i in range(2, B + 1):
    cnt = 0
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:
        sosu.add(i)

# print(sosu)
sit = 1
# 앞에 것들은 무조건 되므로 새로 소수를 만나면 그것을 추가하고
# 썼던 소수면 빼주기
used = set()
for i in range(A, B + 1):
    sit += i - 1
    for j in range(1, i + 1):
        if i % j == 0:
            if j in used:
                sit -= i // j - 1
            else:
                if j in sosu:
                    used.add(j)
    
print(sit)
