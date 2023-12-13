import sys
input = sys.stdin.readline

def dfs(i, target):
    for k in sorted(list(target.keys())):
        print(' ' * i + k)
        dfs(i + 1, target[k])

N = int(input().strip())

# 디렉토리 딕셔너리 용훈이형의 코드를 빼끼기 크하하하하하하하ㅏㅏ하ㅏ
dic = {}
for _ in range(N):
    arr = list(map(str, input().strip().split('\\')))
    target = dic
    
    for word in arr:
        if word not in target:
            target[word] = {}
        target = target[word]
        
# dfs를 통해 출력
dfs(0, dic)