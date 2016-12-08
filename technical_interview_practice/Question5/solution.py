class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def question5(self, ll, m):

        if not ll:
            return None

        if self.head.data != ll.data:
            return None

        runner = self.head
        for i in range(m):
            if not runner:
                break
            runner = runner.next

        slow = self.head
        while runner:
            runner = runner.next
            slow = slow.next

        return slow.data

ll = LinkedList()
ll.addNode(12)
ll.addNode(8)
ll.addNode(5)
ll.addNode(20)
print ll.question5(Node(20), 3) # 5

ll = LinkedList()
ll.addNode(20)
ll.addNode(4)
ll.addNode(15)
ll.addNode(35)
print ll.question5(Node(35), 5) # 35

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(6)
ll.addNode(5)
print ll.question5(Node(5), 2) # 2

ll = LinkedList()
ll.addNode(20)
print ll.question5(Node(35), 5) # None
