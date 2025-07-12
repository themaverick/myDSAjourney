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

def findHeight(root):
    if root is None:
        return 0

    return max(findHeight(root.left), findHeight(root.right)) + 1

def findBalanced(root):
    ## return balanced, height
    if root is None:
        return (True, 0)
    
    right = findBalanced(root.right)
    left = findBalanced(root.left)
    return (right[0] and left[0] and abs(left[1] - right[1]) <= 1, max(right[1], left[1]) + 1)

root = buildTree()

level_order_traversal(root)


print(findBalanced(root))


