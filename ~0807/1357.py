X, Y = map(str, input().split())


# x 와 y 의 길이를 구한다.
len_x = 0
for i in X:
    len_x += 1

len_y = 0
for j in Y:
    len_y += 1

# 역순으로 x 와 y 를 만들어준다.
new_x = ''
for k in range(len_x - 1, -1, -1):
    new_x += X[k]

new_y = ''
for l in range(len_y - 1, -1, -1):
    new_y += Y[l]

# x 와 y 의 합을 구한다.
sum_xy = int(new_x) + int(new_y)
sum_xy = str(sum_xy)

# 합의 순서를 다시 바꿔준다.
len_sum_xy = 0
for m in sum_xy:
    len_sum_xy += 1

new_xy = ''
for n in range(len_sum_xy - 1, -1, -1):
    new_xy += sum_xy[n]

print(int(new_xy))
