from itertools import combinations_with_replacement

N = int(input())

# 이거 그냥 서로다른 4개에서 N개를 중복 선택하는 중복조합이네 easy
# combinations_with_replacement이거 쓰면 중복조합일듯
# 그래서 중복조합들을 다 구한 뒤 얘네들을 돌면서 이것들의 합을 또 set로 중복제거
arr = [1, 5, 10, 50]
total = set()
# print(list(combinations_with_replacement(arr, N)))
for i in list(combinations_with_replacement(arr, N)):
    total.add(sum(i))
# print(arr)
print(len(total))