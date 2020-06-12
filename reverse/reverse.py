class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        current = self.head
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
        # trying to get this to work recursively
        # prev = None
        # current = self.head

        # if current is None:
        #     return
        # # list with 2 elements
        # elif self.head.next_node is None:
        #     return current
        # else:
        #     # here implement the recursive call

        #     reversed = self.reverse_list(node)

        #     return reversed
