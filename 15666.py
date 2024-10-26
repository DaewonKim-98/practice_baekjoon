from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))

nses = []
for s in combinations_with_replacement(arr, M):
  ns = list(s)
  ns.sort()
  ns = tuple(ns)
  nses.append(ns)
nses = set(nses)
nses = list(nses)
nses.sort()
for s in nses:
  for num in s:
    print(num, end=' ')
  print()