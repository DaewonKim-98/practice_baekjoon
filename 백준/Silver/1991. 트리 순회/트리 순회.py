import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}
for _ in range(N):
    arr = list(map(str, input().split()))
    tree[arr[0]] = [arr[1], arr[2]]

# 전위 순회
def preorder_travel(root):
    if root != '.':
        print(root, end='')
        preorder_travel(tree[root][0])
        preorder_travel(tree[root][1])
# 중위 순회
def inorder_travel(root):
    if root != '.':
        inorder_travel(tree[root][0])
        print(root, end='')
        inorder_travel(tree[root][1])
# 후위 순회
def postorder_travel(root):
    if root != '.':
        postorder_travel(tree[root][0])
        postorder_travel(tree[root][1])
        print(root, end='')

preorder_travel('A')
print()
inorder_travel('A')
print()
postorder_travel('A')