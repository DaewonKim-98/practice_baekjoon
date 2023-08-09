N = list(input())

sum_n = 0
for i in N:
    sum_n += int(i)

# 수의 마지막이 0이고 각 자리의 숫자의 합이 3의 배수이면 30의 배수
# 즉 둘 중 하나라도 성립이 안되면 -1 출력
if '0' not in N or sum_n % 3 != 0:
    print(-1)

# 아니면 30의 배수라는 소리이므로 내림차순으로 정렬한 것이 가장 크다.
else:
    # 1의 자리의 수들을 나열하는 것이므로 
    zlist = [0] * 10
    # zlist의 num 인덱스에 1을 추가해주면 num의 개수를 알 수 있다.
    for num in N:
        zlist[int(num)] += 1

    # 큰 수부터 정렬해야 하므로 뒤에서부터
    for j in range(9, -1, -1):
        if zlist[j] != 0:
            # num의 개수만큼 j를 출력하면 내림차순으로 정렬한 것
            for k in range(zlist[j]):
                print(j, end='')

