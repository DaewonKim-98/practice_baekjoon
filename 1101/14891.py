from collections import deque

gear1 = deque(map(int, input()))
gear2 = deque(map(int, input()))
gear3 = deque(map(int, input()))
gear4 = deque(map(int, input()))


K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    if num == 1:
        # 일단 1번 회전
        copy1 = list(gear1)[:]
        if dir == 1:
            gear1.appendleft(gear1.pop())
        else:
            gear1.append(gear1.popleft())
        # 1, 2가 다르면 2번도 회전
        if copy1[2] != gear2[6]:
            copy2 = list(gear2)[:]
            if dir == -1:
                gear2.appendleft(gear2.pop())
            else:
                gear2.append(gear2.popleft())
            # 2, 3이 다르면 3번도 회전
            if copy2[2] != gear3[6]:
                copy3 = list(gear3)[:]
                if dir == 1:
                    gear3.appendleft(gear3.pop())
                else:
                    gear3.append(gear3.popleft())
                # 3, 4가 다르면 4번도 회전
                if copy3[2] != gear4[6]:
                    if dir == -1:
                        gear4.appendleft(gear4.pop())
                    else:
                        gear4.append(gear4.popleft())
    elif num == 2:
        # 일단 2번 회전
        copy2 = list(gear2)[:]
        if dir == 1:
            gear2.appendleft(gear2.pop())
        else:
            gear2.append(gear2.popleft())
        # 1, 2가 다르면 1번도 회전
        if gear1[2] != copy2[6]:
            if dir == -1:
                gear1.appendleft(gear1.pop())
            else:
                gear1.append(gear1.popleft())
        # 2, 3이 다르면 3번도 회전
        if copy2[2] != gear3[6]:
            copy3 = list(gear3)[:]
            if dir == -1:
                gear3.appendleft(gear3.pop())
            else:
                gear3.append(gear3.popleft())
            # 3, 4가 다르면 4번도 회전
            if copy3[2] != gear4[6]:
                if dir == 1:
                    gear4.appendleft(gear4.pop())
                else:
                    gear4.append(gear4.popleft())
    elif num == 3:
        # 일단 3번 회전
        copy3 = list(gear3)[:]
        if dir == 1:
            gear3.appendleft(gear3.pop())
        else:
            gear3.append(gear3.popleft())
        # 2, 3이 다르면 2번도 회전
        if gear2[2] != copy3[6]:
            copy2 = list(gear2)[:]
            if dir == -1:
                gear2.appendleft(gear2.pop())
            else:
                gear2.append(gear2.popleft())
            # 1, 2가 다르면 1번도 회전
            if gear1[2] != copy2[6]:
                if dir == 1:
                    gear1.appendleft(gear1.pop())
                else:
                    gear1.append(gear1.popleft())
        # 3, 4가 다르면 4번도 회전
        if copy3[2] != gear4[6]:
            if dir == -1:
                gear4.appendleft(gear4.pop())
            else:
                gear4.append(gear4.popleft())
    else:
        # 일단 4번 회전
        copy4 = list(gear4)[:]
        if dir == 1:
            gear4.appendleft(gear4.pop())
        else:
            gear4.append(gear4.popleft())
        # 3, 4가 다르면 3번도 회전
        if gear3[2] != copy4[6]:
            copy3 = list(gear3)[:]
            if dir == -1:
                gear3.appendleft(gear3.pop())
            else:
                gear3.append(gear3.popleft())
            # 2, 3이 다르면 2번도 회전
            if gear2[2] != copy3[6]:
                copy2 = list(gear2)[:]
                if dir == 1:
                    gear2.appendleft(gear2.pop())
                else:
                    gear2.append(gear2.popleft())
                # 1, 2가 다르면 1번도 회전
                if gear1[2] != copy2[6]:
                    if dir == -1:
                        gear1.appendleft(gear1.pop())
                    else:
                        gear1.append(gear1.popleft())
    # print(gear1)
    # print(gear2)
    # print(gear3)
    # print(gear4)

result = gear1[0] + gear2[0] * 2 + gear3[0] * 4 + gear4[0] * 8
print(result)
            
        
    