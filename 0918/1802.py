import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def fold(words):
    global result
    if len(words) == 1:
        return
    middle = len(words) // 2
    for i in range(1, middle + 1):
        if int(words[middle - i]) + int(words[middle + i]) != 1:
            result = 'NO'
            return
    left = words[:middle]
    right = words[middle + 1:]
    fold(left)
    fold(right)

T = int(input().strip())
for case in range(1, T + 1):
    # 가운데 숫자를 두고 양 옆이 대칭이면 동호처럼 만들 수 있음
    result = 'YES'
    words = list(input().strip())
    fold(words)

    print(result)