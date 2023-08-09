T = int(input())

for case in range(1, T + 1):
    N = int(input())
    if N == 1 or N == 0:
        print(2)
        
    else:
        while True:

            # 자신을 제외하고 나눴을 때 나머지가 0인게 1밖에 없는게 소수
            remain = 1
            # 그래서 자기보다 작은 것 중 2부터 시작해서 0이 되는게 있으면 탈출해서 버림
            for i in range(2, int(N ** (1/2)) + 1):
                if N % i == 0:
                    remain = i
                    break

            # 소수인게 판단되면 N 을 출력하고 탈출
            if remain == 1:
                print(N)
                break
            # 아니면 N에 1을 추가해서 큰 소수를 찾는다.
            else:
                N += 1

    