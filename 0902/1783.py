import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 이동 횟수가 4보다 클 때는 무조건 가로를 한칸 씩 다 갈 수 있으므로
# 나이트의 이동 방법을 한 번씩 사용했다고 치면 M - 2가 될 수 밖에 없고
if N >= 3 and M >= 7:
    print(M - 2)
    
# 이동 횟수가 4보다 작을 때는 N이 3보다 크거나 같으면 왔다갔다를 할 수 있으므로
# M이 갈 수 있는 최대 개수
elif N >= 3:
    # 만약 M이 4보다 크면 모든 이동 방법을 다 사용할 수 없는 경우이므로 4를 출력
    if M > 4:
        print(4)
    else:
        print(M)
# N이 2이면 오른쪽으로 2칸씩 밖에 갈 수 없으므로
elif N == 2:
    # 만약 M이 8보다 크면 모든 이동 방법을 다 사용할 수 없는 경우이므로 4를 출력
    if M > 8:
        print(4)
    else:
        print((M - 1) // 2 + 1)
# 마지막으로 N이 1이면 아예 못가므로
else:
    print(1)