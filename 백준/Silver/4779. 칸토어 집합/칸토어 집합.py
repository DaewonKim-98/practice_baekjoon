import sys
input = sys.stdin.readline

def kanto(N):
    # N 이 1일 때 재귀 종료
    if N == 1:
        return '-'
    else:
        result = kanto(N // 3) + ' ' * (N // 3) + kanto(N // 3)
        return result

while True:
    try:
        N = int(input())
        N = 3 ** N
        print(kanto(N))
        
    except:
        break
    