def get_left_child(T, node):
    n = len(T)
    row = T[node]
    for i in range(n):
        if row[i] == 1 and i < node:
            return i
    return None


def get_right_child(T, node):
    n = len(T)
    row = T[node]
    for i in range(n):
        if row[i] == 1 and i > node:
            return i
    return None


"""
By using recursive approach the space complexity is O(n) where n is the number of calls we make to the function
"""


def least_common_ancestor(parent, node1_val, node2_val):
    left = get_left_child(T, parent)  # O(n)
    right = get_right_child(T, parent)  # O(n)

    if left is None or right is None:
        return None

    if parent > node1_val and parent > node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(left, node1_val, node2_val)
    elif parent < node1_val and parent < node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(right, node1_val, node2_val)

    return parent

"""
By using iterative approach we reduced the space complexity to be O(1)
"""


def least_common_ancestor_itr(parent, node1_val, node2_val):

    while True:
        left = get_left_child(T, parent)  # O(n)
        right = get_right_child(T, parent)  # O(n)

        if left is None or right is None:
            return None

        if parent > node1_val and parent > node2_val:
            # if parent larger than both nodes, then we should reduce (go left)
            parent = left
        elif parent < node1_val and parent < node2_val:
            # if parent larger than both nodes, then we should reduce (go left)
            parent = right
        else:
            break

    return parent


def question4(T, r, n1, n2):
    if not T or T == [[]]:
        return

    n = len(T)
    if r >= n or n1 >= n or n2 > n:
        return

    lca = least_common_ancestor_itr(r, n1, n2)

    return lca


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
print question4(T, 3, 1, 4) # 3

T = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0]]
print question4(T, 2, 5, 0) # 2


T = [[0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0]]
print question4(T, 5, 1, 6)  # 5

T = [[0, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0]]
print question4(T, 5, 1, 3)  # None

T = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0]]
print question4(T, 5, 1, 3)  # 1

