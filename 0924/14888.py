import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def calculator(i, operator):
    global max_result
    global min_result
    global result
    # 연산이 끝나면 갱신
    if i == N - 1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    else:
        # 연산자를 돌면서 계산
        for j in range(4):
            # 연산자가 남아있으면 계산
            if operator[j] > 0:
                if j == 0:
                    # 합
                    origin = result
                    result = result + arr[i + 1]
                    # 연산자 제거
                    operator[j] -= 1
                    # 재귀
                    calculator(i + 1, operator)
                    # 다시 연산자 복구
                    operator[j] += 1
                    result = origin
                elif j == 1:
                    # 차
                    origin = result                    
                    result = result - arr[i + 1]
                    # 연산자 제거
                    operator[j] -= 1
                    # 재귀
                    calculator(i + 1, operator)
                    # 다시 연산자 복구
                    operator[j] += 1
                    result = origin
                elif j == 2:
                    # 곱
                    origin = result
                    result = result * arr[i + 1]
                    # 연산자 제거
                    operator[j] -= 1
                    # 재귀
                    calculator(i + 1, operator)
                    # 다시 연산자 복구
                    operator[j] += 1
                    result = origin
                elif j == 3:
                    # 나눗셈
                    origin = result
                    if result >= 0:
                        result = result // arr[i + 1]
                    else:
                        result = abs(result) // arr[i + 1]
                        result = 0 - result
                    # 연산자 제거
                    operator[j] -= 1
                    # 재귀
                    calculator(i + 1, operator)
                    # 다시 연산자 복구
                    operator[j] += 1
                    result = origin
                    
                

N = int(input().strip())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

i = 0
max_result = -1000000000
min_result = 1000000000
result = arr[0]
calculator(i, operator)
print(max_result)
print(min_result)