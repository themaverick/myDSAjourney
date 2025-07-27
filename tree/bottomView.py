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


def bottomView(root):
    if root is None:
        return
    
    # Queue stores tuples of (node, horizontal_distance)
    queue = deque()
    queue.append((root, 0))

    top_nodes = dict()

    while queue:
        node, h_dist = queue.popleft()

        # if h_dist not in top_nodes:
        top_nodes[h_dist] = node.data

        if node.left:
            queue.append((node.left, h_dist - 1))
        if node.right:
            queue.append((node.right, h_dist + 1))

    # Sorting by horizontal distance
    for key in sorted(top_nodes.keys()):
        print(top_nodes[key])


## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

bottomView(root)

# print(printVertical(root, 0, 0))

print(20 * "*")

# level_order_traversal(root) 