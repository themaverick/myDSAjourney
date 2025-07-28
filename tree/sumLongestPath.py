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


def sumLongestPath(root, sum, level, ans):
    if root is None:
        return
    
    sum += root.data

    if not(root.left) and not(root.right):
        if len(ans) == 1:
            if (ans[0][0] < level) or (ans[0][0] == level and sum > ans[0][1]):
                ans[0] = (level, sum)
        else:
            ans.append((level, sum))


    sumLongestPath(root.left, sum, level+1, ans)
    sumLongestPath(root.right, sum, level+1, ans)


## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

ans = []
sumLongestPath(root, 0, 0, ans)
print(ans[0][1])

# print(printVertical(root, 0, 0))

print(20 * "*")

# level_order_traversal(root) 