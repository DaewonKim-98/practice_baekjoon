import sys
input = sys.stdin.readline

def w(a, b, c):
    for k in range(a + 1):
        for i in range(b + 1):
            for j in range(c + 1):
                if k < i and i < j:
                    if k <= 0 or i <= 0 or j <= 0:
                        w_dic[(k, i, j)] = w_dic[(k - 1, i, j)] = w_dic[(k, i - 1, j)] = w_dic[(k, i, j - 1)] = w_dic[k - 1, i, j - 1] = w_dic[k, i - 1, j - 1] = w_dic[k - 1, i - 1, j] = w_dic[k - 1, i - 1, j - 1] = 1
                    w_dic[(k, i, j)] = w_dic[(k, i, j - 1)] + w_dic[(k, i - 1, j - 1)] - w_dic[(k, i - 1, j)]
                    if k <= 0 or i <= 0 or j <= 0:
                        w_dic[(k, i, j)] = w_dic[(k - 1, i, j)] = w_dic[(k, i - 1, j)] = w_dic[(k, i, j - 1)] = w_dic[k - 1, i, j - 1] = w_dic[k, i - 1, j - 1] = w_dic[k - 1, i - 1, j] = w_dic[k - 1, i - 1, j - 1] = 1
                    
                else:
                    if k <= 0 or i <= 0 or j <= 0:
                        w_dic[(k, i, j)] = w_dic[(k - 1, i, j)] = w_dic[(k, i - 1, j)] = w_dic[(k, i, j - 1)] = w_dic[k - 1, i, j - 1] = w_dic[k, i - 1, j - 1] = w_dic[k - 1, i - 1, j] = w_dic[k - 1, i - 1, j - 1] = 1
                    w_dic[k, i, j] = w_dic[k-1, i, j] + w_dic[k-1, i-1, j] + w_dic[k-1, i, j-1] - w_dic[k-1, i-1, j-1]
                    if k <= 0 or i <= 0 or j <= 0:
                        w_dic[(k, i, j)] = w_dic[(k - 1, i, j)] = w_dic[(k, i - 1, j)] = w_dic[(k, i, j - 1)] = w_dic[k - 1, i, j - 1] = w_dic[k, i - 1, j - 1] = w_dic[k - 1, i - 1, j] = w_dic[k - 1, i - 1, j - 1] = 1

    else:
        return w_dic[a, b, c]

w_dic = {}
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        w_dic[20, 20, 20] = 1048576
        if a <= 0 or b <= 0 or c <= 0:
            print(f'w({a}, {b}, {c}) = {1}')
        
        elif a > 20 or b > 20 or c > 20:
            print(f'w({a}, {b}, {c}) = {w_dic[20, 20, 20]}')
        else:
            print(f'w({a}, {b}, {c}) = {w(a, b, c)}')