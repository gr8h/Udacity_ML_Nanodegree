""" question1 ---------------------------"""

"""
First solution by sorting and comparing each window
Time: O(n log n)
Space: O(1)
"""
def question1_nlogn(s, t):
    if not s or not t or s == "" or t == "":
        return False

    if type(s) != str and type(t) != str:
        return False

    if len(t) > len(s):
        return False

    s = s.lower()
    t = sorted(t.lower())
    window_size = len(t)
    num_of_windows = len(s) - len(t) + 1

    for win in range(num_of_windows):
        current_window = sorted(s[win:win+window_size])
        if current_window == t:
            return True

    return False


"""
Second solution by assuming that the string input is ASCII so the max value will be 256,
The compare a counter by maintaining a window of target input size
"""
def question1(s, t):
    if not s or not t or s == "" or t == "":
        return False

    if type(s) != str and type(t) != str:
        return False

    if len(t) > len(s):
        return False

    s = s.lower()
    t = t.lower()

    t_count = [0] * 256
    s_count = [0] * 256

    for i in range(len(t)):
        t_count[ord(t[i])] += 1
        s_count[ord(s[i])] += 1

    win = len(t)
    while win <= len(s):
        if compareCounter(t_count, s_count):
            return True

        s_count[ord(s[win])] += 1
        s_count[ord(s[win - len(t)])] -= 1
        win += 1

    return False

def compareCounter(t_count, s_count):
    return t_count == s_count

    # for i in range(len(t_count)):
    #     if t_count[i] != s_count[i]:
    #         return False
    # return True


print question1("udacity", "ad")  # True
print question1("udacitty", "yt")  # True
print question1("nAnodegree", "gedo")  # True
print question1("helloworlD", "dlr")  # True
print question1("", "xyz")  # False
print question1("xyz", "")  # False
print question1("", "")  # False
print question1(None, None)  # False
print question1(123, 456)  # False


""" question2 ---------------------------"""


def question2(a):
    if not a:
        return None

    if len(a) == 1:
        return a

    # create a matrix of size n x n
    n = len(a)
    w = 0
    res = ""
    tbl = [[0 for y in range(n)] for x in range(n)]

    # for each string of size 1 there will be max palindrome of size 1
    for i in range(n):
        tbl[i][i] = 1

    for i in range(1, n):
        for k in range(n - i):
            x = k
            y = k + i

            # check if the the outer characters are the same
            if a[x] == a[y]:
                # we sum the last max palindrome length + 2
                tbl[x][y] = 2 + tbl[x + 1][y - 1]
                # if the length larger that the max len that we reached so far
                if w < y - x + 1:
                    w = x - y + 1
                    # update the longest substring accordingly
                    res = a[x: y + 1]
            else:
                # select the max palindrome so far
                tbl[x][y] = max(tbl[x - 1][y], tbl[x][y - 1])
    return res


print question2("bananas")
print question2("babad")
print question2("cbbd")
print question2("xyzqwer")

""" question3 ---------------------------"""

import heapq
import sys


def question3(G, start=None):
    if not G or G == [[]]:
        return

    # heap
    pq = []
    # store vertex to edge
    vertexToEdge = {}
    # final result MST
    result = []

    # set the start vertex
    for vertex in G:
        if start is None or vertex == start:
            heapq.heappush(pq, (0, vertex))
            start = vertex
        else:
            heapq.heappush(pq, (sys.maxsize, vertex))

    # create a dic for easy lookup
    pq_lookup = dict([(v, w) for (w, v) in pq])

    # while heap is not empty
    while pq:
        # get the edge with the min weight
        current_w, current_v = heapq.heappop(pq)
        del pq_lookup[current_v]

        # if the current edge is in vertexToEdge then this is our min edge
        if current_v in vertexToEdge:
            result.append(vertexToEdge[current_v])

        # get the current edge neighbors
        for edge_v, edge_w in G[current_v]:
            # check if the this neighbor edge in our heap and its weight is less that the current value
            if edge_v in pq_lookup and pq_lookup[edge_v] > edge_w:
                # update the heap with the new min weight
                updateHeap(pq, pq_lookup, edge_v, edge_w)
                # add this edge to vertexToEdge
                vertexToEdge[edge_v] = (current_v, edge_v)

    return result


def updateHeap(pq, pq_lookup, vertex, weight):
    for i in range(len(pq)):
        w, v = pq[i]
        if v == vertex:
            del pq[i]
            break
    pq_lookup[vertex] = weight
    heapq.heappush(pq, (weight, vertex))


G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}

print question3(G)
# [('A', 'B'), ('B', 'C')]

G = dict(A=[('D', 1), ('B', 3)],
         B=[('A', 3), ('D', 3), ('C', 1)],
         C=[('B', 1), ('D', 1), ('E', 5), ('F', 4)],
         D=[('A', 1), ('B', 3), ('C', 1), ('E', 6)],
         E=[('D', 6), ('C', 5), ('F', 2)],
         F=[('E', 2), ('C', 4)])

print question3(G)
# [('A', 'D'), ('D', 'C'), ('C', 'B'), ('C', 'F'), ('F', 'E')]

G = {'A': [('D', 2)],
     'B': [('E', 2), ('H', 5)],
     'C': [('F', 5)]}

print question3(G)
# []

G = {}

print question3(G)
# []

""" question4 ---------------------------"""

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


def least_common_ancestor(parent, node1_val, node2_val):
    left = get_left_child(T, parent)
    right = get_right_child(T, parent)

    if left is None or right is None:
        return None

    if parent > node1_val and parent > node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(left, node1_val, node2_val)
    elif parent < node1_val and parent < node2_val:
        # if parent larger than both nodes, then we should reduce (go left)
        return least_common_ancestor(right, node1_val, node2_val)

    return parent


def question4(T, r, n1, n2):
    if not T or T == [[]]:
        return

    n = len(T)
    if r >= n or n1 >= n or n2 > n:
        return

    lca = least_common_ancestor(r, n1, n2)

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
print question4(T, 2, 5, 0)


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



""" question5 ---------------------------"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Build the linkedlist
    def addNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def question5(self, ll, m):
        # check linkedlist is not empty and ll is the start node
        if not ll:
            return None

        if self.head.data != ll.data:
            return None
        # start from the head, create two pointers
        runner = self.head
        slow = self.head

        # traverse the first pointer to the length of m
        for i in range(m):
            # or until the pointer is null which will indicate that m is larger than the linkedlist
            if not runner:
                break
            runner = runner.next
        # then, traverse both pointers until the first pointer is null
        while runner:
            runner = runner.next
            slow = slow.next

        return slow.data


ll = LinkedList()
ll.addNode(12)
ll.addNode(8)
ll.addNode(5)
ll.addNode(20)
print ll.question5(Node(20), 3)  # 5

ll = LinkedList()
ll.addNode(20)
ll.addNode(4)
ll.addNode(15)
ll.addNode(35)
print ll.question5(Node(35), 5)  # 35

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(6)
ll.addNode(5)
print ll.question5(Node(5), 2)  # 2

ll = LinkedList()
ll.addNode(20)
print ll.question5(Node(35), 5)  # None
