import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    
    # 출력해야할 문서를 1로 표시한 리스트
    print_list = [0] * N
    print_list[M] = 1

    # 최댓값 인덱스 구하기
    max_idx = 0
    for i in range(N):
        if docs[max_idx] < docs[i]:
            max_idx = i

    # 최댓값 인덱스가 M이 될 때까지 반복을 하며 삭제한다.
    cnt = 0
    while max_idx != M:
        for idx in range(max_idx):
            docs.append(docs.pop(0))
            print_list.append(print_list.pop(0))
        docs.pop(0)
        print_list.pop(0)
        cnt += 1

        # M 다시 갱신
        for i in range(len(print_list)):
            if print_list[i] == 1:
                M = i

        # 최댓값 인덱스 다시 갱신
        max_idx = 0
        for i in range(len(docs)):
            if docs[max_idx] < docs[i]:
                max_idx = i

    # while문이 끝났으면 최댓값 인덱스가 M이 되었다는 것이므로 마지막 M을 뽑는 걸 추가
    cnt += 1
    print(cnt)