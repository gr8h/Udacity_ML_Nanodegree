class Node:
    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildTreeNodes(T, node):
    n = len(T)
    for i in range(n):
        row = T[node.value]
        if row[i] == 1:
            if i > node.value:
                node.right = i
                buildTreeNodes(T, Node(i))
            if i < node.value:
                node.left = i
                buildTreeNodes(T, Node(i))


def least_common_ancestor(parent, node1_val, node2_val):
    if not parent.left or not parent.right:
        return None

    if parent.value > node1_val and parent.value > node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(parent.left, node1_val, node2_val)
    elif parent.value < node1_val and parent.value < node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(parent.right, node1_val, node2_val)

    return parent


def question4(T, r, n1, n2):
    if not T or T == [[]] or not r or not n1 or not n2:
        return

    n = len(T)
    if r >= n or n1 >= n or n2 > n:
        return

    parent_node = Node(r)
    buildTreeNodes(T, parent_node)

    lca = least_common_ancestor(parent_node, n1, n2)

    return lca.value


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
print question4(T, 3, 1, 4) # 3

T = [[0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1],
     [0, 0, 0, 0]]
print question4(T, 1, 1, 3) # 1

T = [[0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]
print question4(T, 5, 1, 6)  # 5
