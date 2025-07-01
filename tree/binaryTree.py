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

def pre_order_traversal(root):
    if root == None:
        return
    
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

def in_order_traversal(root):
    if root == None:
        return
    
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)

def post_order_traversal(root):
    if root == None:
        return
    
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data)

def level_order_traversal(root):
    queue = []
    queue.append(root)
    queue.append(None)

    while queue:
        
        element = queue.pop(0)
        if element is None:
            print()
            if queue:
                queue.append(None)
        else:
            print(element.data, end=" ")

            if element.left:
                queue.append(element.left)

            if element.right:
                queue.append(element.right)


    

## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

post_order_traversal(root)

print(20 * "*")

# level_order_traversal(root)