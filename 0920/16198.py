import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(arr, i, energy, N):
    global max_energy
    # N이 2가 되면 더 이상 에너지를 모을 수 없으므로
    if N == 2:
        if max_energy < energy:
            max_energy = energy
        return

    else:
        # x번째 에너지 구슬 선택
        for x in range(1, N - 1):
            plus_energy = arr[x - 1] * arr[x + 1]
            v = arr.pop(x)
            dfs(arr, i + 1, energy + plus_energy, N - 1)
            # 다시 x 채우기
            arr.insert(x, v)



N = int(input().strip())
arr = list(map(int, input().split()))


max_energy = 0
energy = 0
i = 0
dfs(arr, i, energy, N)
print(max_energy)