class Node:
    def __init__(self, element):
        self.data = element
        self.right = None
        self.left = None


def buildTree():
    data = int(input("Enter the element: "))
    root = Node(data)

    queue = [root]

    while queue:
        current = queue.pop(0)

        
        left_data = int(input(f"Enter the element to the left of {current.data}: "))
        if left_data != -1:
            current.left = Node(left_data)
            queue.append(current.left)

        right_data = int(input(f"Enter the element to the right of {current.data}: "))
        if right_data != -1:
            current.right = Node(right_data)
            queue.append(current.right)

    return root
        
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

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
        return False

    if root1.data == root2.data:
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

    return False

root1 = buildTree()
root2 = buildTree()

# level_order_traversal(root)


print(isIdentical(root1, root2))


