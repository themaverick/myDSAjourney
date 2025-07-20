from collections import deque

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

def printZigzag(root, l2r):
    queue = []
    queue.append(root)
    queue.append(None)

    while queue:
        
        element = queue.pop(0)
        if element is None:
            l2r = not(l2r)
            print()
            if queue:
                queue.append(None)
        else:
            print(element.data, end=" ")

            if l2r:
                if element.left:
                    queue.append(element.left)

                if element.right:
                    queue.append(element.right)

            else:  
                if element.right:
                    queue.append(element.right)  

                if element.left:
                    queue.append(element.left)

def printZigzag(root):
    if not root:
        return

    dq = deque()
    dq.append(root)
    left_to_right = True

    while dq:
        level_size = len(dq)
        level_nodes = []

        for _ in range(level_size):
            node = dq.popleft()
            level_nodes.append(node.data)

            # Enqueue children normally (left to right)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        # Print the current level
        if left_to_right:
            print(' '.join(map(str, level_nodes)))
        else:
            print(' '.join(map(str, reversed(level_nodes))))

        # Flip direction
        left_to_right = not left_to_right

root = buildTree()

printZigzag(root)


