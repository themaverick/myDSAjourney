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

def printLeaves(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end = " ")
        return
    
    printLeaves(root.left)
    printLeaves(root.right)

def printBoundary(root):
    cur = root

    ## printing the left part
    if cur is None:
        return
    elif cur.left is None:
        print(cur.data, end = " ")
    else:
        while cur.left is not None or cur.right is not None:
            print(cur.data, end=" ")
            if cur.left is not None:
                cur = cur.left
            else:
                cur = cur.right

    ## printing the leaves
    printLeaves(root)


    ##printing right part opposite way
    cur2 = root
    rightPart = []
    while cur2.right is not None or cur2.left is not None:
        rightPart.append(cur2.data)
        if cur2.right is None:
            cur2 = cur2.left
        else:
            cur2 = cur2.right
    
    rightPart = rightPart[1:]

    for i in rightPart[::-1]:
        print(i, end = " ")
    print()
    return



## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

printBoundary(root)

print(20 * "*")

# level_order_traversal(root)