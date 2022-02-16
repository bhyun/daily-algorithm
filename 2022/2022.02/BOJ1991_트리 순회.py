def preorder(node):
    if node == ".":
        return
    print(node, end="")
    left, right = tree[node][0], tree[node][1]
    preorder(left)
    preorder(right)

def inorder(node):
    if node == ".":
        return
    left, right = tree[node][0], tree[node][1]
    inorder(left)
    print(node, end="")
    inorder(right)

def postorder(node):
    if node == ".":
        return
    left, right = tree[node][0], tree[node][1]
    postorder(left)
    postorder(right)
    print(node, end="")


n = int(input())
tree = dict()
for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")