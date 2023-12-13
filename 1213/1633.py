# 딱봐도 dp 세상에서 dp라는 문제들을 다 박멸시켜야 한다고 생각한다.
dp = [[0] * 16 for _ in range(16)]
while True:
    try:
        white, black = map(int, input().split())
        # dp.append([white, black])
        # 뒤에서부터 바뀌게 넣으면 가장 앞에 있는게 가장 큰 것으로 바뀌면서
        # 자연스럽게 dp가 가장 큰 수들의 합으로 바뀜 근데 왜 안되냐
        # for r in range(15, 0, -1):
        #     for c in range(15, 0, -1):
        #         # 백 능력치가 더 큰 놈이면
        #         if white > black:
        #             dp[r][c] = max(dp[r][c], dp[r - 1][c] + white)
        #         # 검 능력치가 더 큰놈이면
        #         else:
        #             dp[r][c] = max(dp[r][c], dp[r][c - 1] + black)
        # 아 위에처럼 하면 마지막 c에서 하나가 안더해짐
        # 그니까 dp가 올바르게 안만들어지고 섞여서 만들어지는듯
        # 처음부터 다시 만들어보자 0일때까지하고 dp[0][1]이 black 1개가 되도록
        for r in range(15, -1, -1):
            for c in range(15, -1, -1):
                # 백 쭉
                if r > 0:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c] + white)
                # 검 쭉 elif하면 안댐 하 된다 dp 그냥 진짜 박멸해야한다 개빡친다
                if c > 0:
                    dp[r][c] = max(dp[r][c], dp[r][c - 1] + black)
    except:
        print(dp)
        break
    