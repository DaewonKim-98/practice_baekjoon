import copy
from collections import deque

change = [{(0, 0), (0, 1), (1, 0)},
          {(0, 0), (0, 1), (0, 2), (1, 1)},
          {(0, 1), (0, 2), (1, 2)},
          {(0, 0), (1, 0), (2, 0), (1, 1)},
          {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1),},
          {(0, 2), (1, 1), (1, 2), (2, 2)},
          {(1, 0), (2, 0), (2, 1),},
          {(1, 1), (2, 0), (2, 1), (2, 2)},
          {(1, 2), (2, 1), (2, 2)},
          ]


def bfs():
    q = deque()
    q.append((arr, 0))
    
    while q:
        lst, cnt = q.popleft()
        # 만약 모두 바꾸어 화이트보드로 바꼈으면 끝
        if lst == white_board:
            return cnt
        # 모든 클릭을 다 돌면서 다 바꾸면서 횟수 세기
        for i in range(9):
            new_lst = copy.deepcopy(lst)
            # 검은색 흰색 바꾸는 작업
            for j in change[i]:
                if new_lst[j[0]][j[1]] == '*':
                    new_lst[j[0]][j[1]] = '.'
                else:
                    new_lst[j[0]][j[1]] = '*'
            # 만들어졌던 보드가 아니면
            if new_lst not in visited:
                visited.append(new_lst)
                q.append((new_lst, cnt + 1))
                    
                
    
    
P = int(input())
for case in range(1, P + 1):
    arr = [list(input()) for _ in range(3)]
    white_board = [['.'] * 3 for _ in range(3)]

    # 어떤 칸을 클릭했을 때 바뀌는 모든 지점들을 세트로 묶어두고 그 지점들이
    # 모두 있을 때 칸들의 색깔을 바꾸는 작업을 계속 하다보면 흰 보드로
    # 바뀔 수 있을 것이라 생각
    # 아씨 이러면 안되네 ㅋㅋㅋㅋ아오 뻘짓 음 그러면 모두를 다 탐색하는
    # 브루트포스?로 그냥 다 탐색하면서 하나씩 그 개수를 추가하는 식으로?
    
    # 한번 만들었던 보드는 다시 안만들어도 되니까 set으로 판단
    visited = []
    print(bfs())