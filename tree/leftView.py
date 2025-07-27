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


# def printVerticalRecursive(root, n_h, queue):
#     if root is None:
#         return
    
#     queue + [(root.data, n_h)]
    
#     if queue:
#         if root.left:
#             printVerticalRecursive(root.left, n_h - 1, queue)
#         if root.right:
#             printVerticalRecursive(queu)


def leftView(root):
    if root is None:
        return
    
    # Queue stores tuples of (node, vertical_distance)
    queue = deque()
    queue.append((root, 0))

    top_nodes = dict()

    while queue:
        node, v_dist = queue.popleft()

        # if v_dist not in top_nodes:
        if v_dist not in top_nodes:
            top_nodes[v_dist] = node.data

        if node.left:
            queue.append((node.left, v_dist - 1))
        if node.right:
            queue.append((node.right, v_dist - 1))

    # Sorting by horizontal distance
    for key in sorted(top_nodes.keys(), reverse=True):
        print(top_nodes[key])

def leftViewRecur(root, level, ans):
    if root is None:
        return
    
    if len(ans) == level:
        ans.append((root.data, level))

    if root.left:
        leftViewRecur(root.left, level+1, ans)
    if root.right:
        leftViewRecur(root.right, level+1, ans)



## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

ans = []
leftViewRecur(root, 0, ans)
print(ans)

# print(printVertical(root, 0, 0))

print(20 * "*")

# level_order_traversal(root) 