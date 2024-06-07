S = list(input())
T = list(input())

# S 에서 T를 만들어야 하니까 아 걍 T에서 S로 돌려라
for _ in range(len(T) - len(S)):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()

if T == S:
    print(1)
else:
    print(0)