a, b, c = map(int, input().split())

# b가 크면 안된다, b가 짝수냐 홀수냐에 따라서 나눠서 생각
# 그냥 이건 답을 볼 수 밖에 없었던 걸까...
def dac(a, b):
    # b가 1이면 그냥 나머지이면 되므로
    if b == 1:
        return a % c
    # 짝수이면 b를 반으로 나눈 것의 나머지를 제곱한 것에서 나머지를 구하면 똑같으므로
    elif b % 2 == 0:
        return (dac(a, b // 2) ** 2) % c
    # 홀수이면
    else:
        return ((dac(a, b // 2) ** 2) * a) % c
    
print(dac(a, b))