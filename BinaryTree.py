class Node:
    def __init__(self, value, left=None, right=None):
        # all private variables
        self.__value = value
        self.__left = None
        self.__right = None

class BinaryTree:
    def __init__(self):
        self.__root=None


    def add(self, value):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__add_helper()

"""
    def __add_helper(self, value, node):
        if value < self.__value:
            if self.__left is None:
                self.__left = Node(value)
            else:
                self.__add_helper(value)
        elif value > self.__value:

"""
