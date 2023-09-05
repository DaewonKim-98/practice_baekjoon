# 카드 색깔과 숫자 리스트
color = []
number = []
for i in range(5):
    a, b = map(str, input().split())
    color.append(a)
    number.append(int(b))

# 숫자 오름차순으로 정렬
number.sort()

# 가장 높은 점수를 만들 수 있는 규칙부터 보기
for i in range(4):
    # 연속이 아니면 break
    if number[i] + 1 != number[i + 1]:
        break

# 연속이면서 카드의 색깔이 모두 같으면
else:
    if len(set(color)) == 1:
        print(900 + number[4])
        exit()

# 2번째
for i in number:
    copy_number = number[:]
    copy_number.remove(i)
    # 하나를 뺐을 때 세트의 개수가 1이면 같은 숫자의 개수가 4개라는 것이므로
    if len(set(copy_number)) == 1:
        print(800 + list(set(copy_number))[0])
        exit()

# 3번째
for i in range(4):
    for j in range(i + 1, 5):
        # 두 개가 같고 세트에서 이것을 빼줬을 때 개수가 1개이면 나머지 숫자가 다 같다는 뜻이므로
        if number[i] == number[j]:
            if len(set(number) - set([number[i]])) == 1:
                if number.count(number[i]) == 2:
                    print(list(set(number) - set([number[i]]))[0] * 10 + number[i] + 700)
                    exit()
                else:
                    print(number[i] * 10 + list(set(number) - set([number[i]]))[0] + 700)
                    exit()

# 4번째
if len(set(color)) == 1:
    print(600 + number[4])
    exit()

# 5번째
# 가장 높은 점수를 만들 수 있는 규칙부터 보기
for i in range(4):
    # 연속이 아니면 break
    if number[i] + 1 != number[i + 1]:
        break

# 연속이면
else:
    print(500 + number[4])
    exit()

# 6번째
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            if number[i] == number[j] == number[k]:
                print(number[i] + 400)
                exit()

# 7번째
for i in range(4):
    for j in range(i + 1, 5):
        for k in range(4):
            for l in range(k + 1, 5):
                if i != k and j != l:
                    if number[i] == number[j] and number[k] == number[l]:
                        print(max(number[j], number[k]) * 10 + min(number[j], number[k]) + 300)
                        exit()

# 8번째
for i in range(4):
    for j in range(i + 1, 5):
        if number[i] == number[j]:
            print(number[j] + 200)
            exit()

# 9번째
print(number[4] + 100)
    