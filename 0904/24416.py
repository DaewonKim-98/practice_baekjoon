import sys
input = sys.stdin.readline

def fib(n):
    global cnt1
    if n ==1 or n ==2:
        return 1
    else:
        cnt1 += 1
        return fib(n - 1) + fib(n - 2)
    
def fibonacci(n):
    global cnt2
    arr = [0] * 41
    arr[1] = arr[2] = 1
    for i in range(3, n):
        arr[i] = arr[i - 1] + arr[i + 1]
        cnt2 += 1
    return arr[n]

n = int(input().strip())
cnt1 = 1
cnt2 = 1
fib(n)
fibonacci(n)
print(f'{cnt1} {cnt2}')