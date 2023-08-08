# 빙고 판을 만든다.
bingo = []
for i in range(5):
    bingo += [list(map(int, input().split()))]

# 빙고 판을 만든다.
chairman = []
for i in range(5):
    chairman += [list(map(int, input().split()))]

# 사회자가 부르는 call 수를 call_cnt로 둔다.
call_cnt = 0
# 사회자가 부르는 것들을 기록
for call in chairman:
    # 첫 행에도 사회자가 5개를 부르니까 반복문으로 돌린다.
    for k in call:
        # 빙고가 되는 개수를 bingo_cnt로 둔다.
        bingo_cnt = 0
        # 사회자가 값을 부를 때마다 call_cnt에 추가해준다.
        call_cnt += 1
        # 빙고판을 돌려서 k인 값은 0으로 지워준다.
        for r in range(5):
            for c in range(5):
                if bingo[r][c] == k:
                    bingo[r][c] = 0

        for r in range(5):
            # 각 행의 지워진 값의 cnt를 세준다.
            cnt = 0
            for c in range(5):
                if bingo[r][c] == 0:
                    cnt += 1
            # 만약 cnt의 값이 5라면 빙고이므로 bingo_cnt에 1을 추가한다.
            if cnt == 5:
                bingo_cnt += 1

        for c in range(5):
            # 각 열의 지워진 값의 cnt를 세준다.
            cnt = 0
            for r in range(5):
                if bingo[r][c] == 0:
                    cnt += 1
            # 만약 cnt의 값이 5라면 빙고이므로 bingo_cnt에 1을 추가한다.
            if cnt == 5:
                bingo_cnt += 1

        # 정대각선의 지워진 값의 cnt를 세준다.
        cnt = 0
        for r in range(5):
            if bingo[r][r] == 0:
                cnt += 1
            # 만약 cnt의 값이 5라면 빙고이므로 bingo_cnt에 1을 추가한다.
        if cnt == 5:
            bingo_cnt += 1

        # 역대각선의 지워진 값의 cnt를 세준다.
        cnt = 0
        for r in range(5):
            if bingo[r][4 - r] == 0:
                cnt += 1
            # 만약 cnt의 값이 5라면 빙고이므로 bingo_cnt에 1을 추가한다.
        if cnt == 5:
            bingo_cnt += 1
        
        nbingo_cnt = bingo_cnt

        # 만약 bingo_cnt 가 3이상 되면 답을 출력
        if bingo_cnt >= 3:
            break
    if bingo_cnt >= 3:
            break
    
print(call_cnt)