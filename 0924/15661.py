import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def sub(i, num, start):
    global min_sub
    # 인원 수에 맞게 되면
    if i == num:
        # 링크 팀은 전체에서 스타트 팀을 뺀 리스트
        link = list(set(people) - set(start))
        # 능력치의 차이는
        # 스타트 팀
        start_strength = 0
        for k in range(num - 1):
            for l in range(k + 1, num):
                start_strength += arr[start[k]][start[l]]
                start_strength += arr[start[l]][start[k]]
        # 링크 팀
        link_strength = 0
        for k in range(N - num - 1):
            for l in range(k + 1, N - num):
                link_strength += arr[link[k]][link[l]]
                link_strength += arr[link[l]][link[k]]
                
        # 차 갱신
        if min_sub > abs(start_strength - link_strength):
            min_sub = abs(start_strength - link_strength)
    
    else:
        if start:
            # 스타트 팀 조합 뽑기
            for j in range(start[i - 1], N):
                if visited[j] == 0:
                    visited[j] = 1
                    sub(i + 1, num, start + [j])
                    visited[j] = 0
        else:
            # 스타트 팀 조합 뽑기
            for j in range(0, N):
                if visited[j] == 0:
                    visited[j] = 1
                    sub(i + 1, num, start + [j])
                    visited[j] = 0
            
                
                

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
people = list(range(N))


visited = [0] * N
# 차의 최소
min_sub = 100 * N
# 같은 팀은 2명부터 N // 2명까지 할 수 있으므로 순열 구하기
for num in range(2, N // 2 + 1):
    i = 0
    start = []
    sub(i, num, start)
    
print(min_sub)