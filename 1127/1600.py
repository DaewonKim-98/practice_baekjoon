from collections import deque
dir_knight = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
