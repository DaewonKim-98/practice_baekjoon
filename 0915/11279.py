import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
heap = deque([0])
cnt = 0

for _ in range(N):
    x = int(input().strip())
    # x가 0일 때
    if x == 0:
        # 배열이 비었을 때
        if cnt == 0:
            print(0)
        # 수가 하나라도 있으면
        elif cnt > 0:
            # 가장 앞에 있는 최대 수 출력
            heap.popleft()
            print(heap.popleft())
            heap.appendleft(0)
            cnt -= 1

            # heap이 2개 이상 남아있으면 가장 마지막 잎의 노드를 루트로 땡긴 후
            # 자식 노드와 크기를 비교하며 재정렬
            if cnt > 1:
                i = 1
                heap.popleft()
                heap.appendleft(heap.pop())
                heap.appendleft(0)

                while i <= cnt:
                    # 자식 노드가 없으면
                    if i * 2 > cnt:
                        break
                    # 자식 노드가 하나이면
                    elif i * 2 + 1 > cnt:
                        # 자식 노드가 자기보다 크면 교체
                        if heap[i] < heap[i * 2]:
                            heap[i], heap[i * 2] = heap[i * 2], heap[i]
                        break
                    # 자식 노드가 2개이면
                    else:
                        # 자식 노드 중에서 큰 것과 교체
                        if heap[i * 2] > heap[i * 2 + 1]:
                            if heap[i] < heap[i * 2]:
                                heap[i], heap[i * 2] = heap[i * 2], heap[i]
                                i *= 2
                            else:
                                break
                        # 자식 노드 중에서 큰 것과 교체
                        else:
                            if heap[i] < heap[i * 2 + 1]:
                                heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                                i = 2 * i + 1
                            else:
                                break

    # x가 0이 아닐 때
    else:
        # 배열이 비어 있으면
        if cnt == 0: 
            heap.append(x)
            cnt += 1
        elif cnt > 0:
            # 들어오는 자식을 부모 노드와 비교해 정렬
            heap.append(x)
            cnt += 1
            i = cnt
            while i > 1:
                if heap[i // 2] < heap[i]:
                    heap[i // 2], heap[i] = heap[i], heap[i // 2]
                    i //= 2
                else:
                    break
