import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = [input().strip() for _ in range(N)]
keywords = set(keywords)

# M을 돌려 키워드가 있으면 없애고 출력
for _ in range(M):
    arr = set(map(str, input().strip().split(',')))
    for keyword in arr:
        if keyword in keywords:
            keywords.remove(keyword)

    print(len(keywords))