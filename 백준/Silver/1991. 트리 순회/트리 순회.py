def preorder(start):
    if start != '.':
        print(start, end='')
        preorder(tree_dict[start][0])
        preorder(tree_dict[start][1])
def inorder(start):
    if start != '.':
        inorder(tree_dict[start][0])
        print(start, end='')
        inorder(tree_dict[start][1])
def postorder(start):
    if start != '.':
        postorder(tree_dict[start][0])
        postorder(tree_dict[start][1])
        print(start, end='')



N = int(input())
tree_dict = {}
for n in range(N):
    p, l_c, r_c = input().split()
    tree_dict[p] = [l_c, r_c]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()