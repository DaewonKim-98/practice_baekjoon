def div(n):
    if n == 0:
        return 1
    if n in dic:
        return dic[n]
    dic[n] = div(n // P) + div(n // Q)
    return dic[n]
    
# 몫끼리 더한 것과 같으므로 재귀로 쭊 하면 또 되려나
# 진짜 이것도 시간초과 나면 뭐 어쩌자는 거지 어케 없애지
# 메모리제이션? 없애는거 뭐더라
# 아 메모이제이션이네 아오 그걸로 하면 될듯
N, P, Q = map(int, input().split())
dic = {}
dic[0] = 1
if N == 0:
    print(1)
    exit()
if N == 1:
    print(2)
    exit()
    
print(div(N))