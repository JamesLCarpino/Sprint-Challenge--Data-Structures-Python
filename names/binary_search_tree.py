"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root
        # 1 check if there is no root
        # if there isn't create the node and park it there
        # we can check this if self is none to see if there is no root
        if self is None:
            self = BSTnode(value)

        # 2 otherwise, there is a root
        else:
            # compare the value to the roots value to determine which direction to go
            if value < self.value:
                # how do we go left?
                # we need to check if there is another node on the left side
                if self.left:
                    # then self.left is a node
                    self.left.insert(value)
                else:
                    # if no self let we can park value here
                    self.left = BSTNode(value)
                # self.left = BSTNode(value)
            # if the value < root's value
            # go left

            else:
                # else the value >= roots value
                # go right
                # how do we go right?
                if self.right:
                    # then self.right is a node
                    self.right.insert(value)
                else:
                    # if no self right we can park value here
                    self.right = BSTNode(value)
                # self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the tree contains the target value it is True

        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        # else the tree doesn't contain the target value there for False

    # Return the maximum value found in the tree
    def get_max(self):
        # go to the right
        # if nothing right to the value than the root must be largest value
        if not self.right:
            return self.value
        else:
            # return a recursive call
            # if using recursion to find an answer then always return a recursive call so that you can return backinto the next level until you hit basecase
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def depth_first_for_each(self, fn):
        # this method specifically does want to traverse every tree node
        # this has to call the fn on self.value
        fn(self.value)

        # how do we propagate to all the other nodes in the tree?
        # is there a left child?
        if self.left:
            # if yes, then call its `for_each` with the same fn
            self.left.depth_first_for_each(fn)
            # is there a right child?
            if self.right:
                # if yes, then call its `for_each` with the same fn
                self.right.depth_first_for_each(fn)

    def iter_depth_first_for_each(self, fn):
        # with depth-first traversal, there's a certain order to when we visit nodes
        # what's that order?
        # init a stack to keep track of the order of nodes we visited
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and left child second
            # to ensure that left is popped off the stack first
            if current_node.right:
                stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
                    # call the fn function on self.value
                    fn(self.value)

    def iter_breadth_first_search(self, fn):
        # breadth first traversal follows FIFO ordering of its nodes
        # init a deque
        q = deque()
        # add the first node to our q
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                    fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print(self.value)

        if node:

            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

        # if self.left:
        #     self.left.in_order_print(self)
        # print(self.value)
        # if self.right:
        #     self.right.in_order_print(self)

        # if node.left:
        #     node.in_order_print(node.left)
        # print(node.value)
        # if node.right:
        #     node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        que = deque()
        # add first node to the que
        que.append(node)

        # loop through the queue
        while len(que) > 0:
            # pop the first node out
            current_node = que.popleft()
            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
            print(current_node.value)

        # --------------------------#
        # while queue:
        #     node = queue.pop(0)
        #     if node not in explored:
        #         explored.append(node)
        #         neighbors = self[node.value]
        #         for neighbor in neighbors:
        #             queue.append(neighbor)
        # return explored

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        # add the first node to our stack
        stack.append(node)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and left child second
            # to ensure that left is popped off the stack first
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
                # call the fn function on self.value
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
