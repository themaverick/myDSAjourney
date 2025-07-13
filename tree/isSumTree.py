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

def isSumTree(root):
    if root.left is None and root.right is None:
        return (True, root.data)


    ## instead of calling it multiple times, call one time and use the values.
    if root.left is None:
        return ((root.data == isSumTree(root.right)[1]) and isSumTree(root.right)[0], isSumTree(root.right)[1] + root.data)
    elif root.right is None:
        return ((root.data == isSumTree(root.left)[1]) and isSumTree(root.left)[0], isSumTree(root.left)[1] + root.data)
    else:
        return ((root.data == isSumTree(root.right)[1] + isSumTree(root.left)[1]) and isSumTree(root.right)[0] and isSumTree(root.left)[0], isSumTree(root.right)[1] + isSumTree(root.left)[1] + root.data)
    

root1 = buildTree()
a = isSumTree(root1)
print(a[0], a[1])


