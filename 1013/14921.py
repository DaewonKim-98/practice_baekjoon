N = int(input())
arr = list(map(int, input().split()))

max_sum = arr[-1] + arr[-2]
min_sum = abs(arr[0] + arr[1])
max_range = max(max_sum, min_sum)
# 0에서 가장 가까운 것들을 찾는 것이므로
# i는 어떤 두 원소의 합의 절댓값 이라고 한다면 0부터 시작하는 i에서
# 어떤 arr의 원소를 뺐을 때 그게 set_arr 안에 있으면 그 i가 B
for i in range(max_range + 1):
    for a in arr:
        new_arr = arr[:]
        new_arr.remove(a)
        set_arr = set(new_arr)
        if i - a in set_arr:
            print(i)
            exit()
        elif - i - a in set_arr:
            print(i, a)
            print(- i)
            exit()