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



def printVertical(root, n_v, n_h):
    if root is None:
        return
    
    queue = []
    queue.append((root, n_v, n_h))
    # queue.append((None, None))

    all_el = dict()

    while len(queue) > 0:

        
        # if el is None:
        #     queue.append((None, None, None))
        #     continue
        element = queue.pop(0)
        el = element[0]
        n_ve = element[1]
        n_ho = element[2]

        if n_ve in all_el.keys():
            if n_ho in all_el[n_ve].keys():
                all_el[n_ve][n_ho].append(el.data)
            else:
                all_el[n_ve][n_ho] = [el.data]
        else:
            all_el[n_ve] = {n_ho: [el.data]}


        if el.left:
            print((el.left, n_ve-1, n_ho-1))
            queue.append((el.left, n_ve-1, n_ho-1))
        if el.right:
            print((el.right, n_ve-1, n_ho+1))
            queue.append((el.right, n_ve-1, n_ho+1))

    return all_el



## 2 4 7 -1 -1 1 -1 -1 6 3 -1 -1 -1

root = None
root = buildTree(root)

print(printVertical(root, 0, 0))

print(20 * "*")

# level_order_traversal(root) 