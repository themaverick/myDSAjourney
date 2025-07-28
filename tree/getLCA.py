from collections import deque

class Node:
    def __init__(self, element):
        self.data = element
        self.right = None
        self.left = None

class binaryTree:
    def __init__(self):
        self.rootNode = None

def buildTree(root):
    data = int(input(f"Enter the element: "))
    root = Node(data)

    if data == -1:
        return None

    print(f"Enter the data to insert on the left of: {data}")
    root.left = buildTree(root.left)
    print(f"Enter the data to insert on the right of: {data}")
    root.right = buildTree(root.right)

    return root


def getPath(curNode, node, path):
    if curNode is None:
        return
    
    path.append(curNode)

    if curNode == node:
        return True

    if getPath(curNode.left, node, path) or getPath(curNode.right, node, path):
        return True
    
    path.pop()
    return False

def getLCA(root, node1, node2):
    if root is None:
        return 
    elif root == node1 or root == node2:
        return root
    
    left = getLCA(root.left, node1, node2)
    right = getLCA(root.right, node1, node2)

    if left and right:
        print(root.data)
        return root
    elif left:
        return left
    elif right:
        return right
    return

## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

# ans1, ans2 = [], []
# getPath(root, root.left.right, ans1)
# getPath(root, root.right.left, ans2)

# for i in ans1:
#     print(i.data, end = " -> ")
# print()
# for i in ans2:
#     print(i.data, end = " -> ")
# print()

# i = -1
# while i >= -len(ans1) and i >= -len(ans2):
#     print(i)
#     if ans1[i] == ans2[i]:
#         print(f"answer node: {ans1[i].data}")
#         break
#     i -= 1

getLCA(root, root.left.right, root.right.left)
# print(printVertical(root, 0, 0))

print(20 * "*")

# level_order_traversal(root) 