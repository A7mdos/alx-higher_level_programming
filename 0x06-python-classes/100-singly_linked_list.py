#!/usr/bin/python3
"""SUIIIII"""


class Node:
    """SUIIIII"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """SUIIIII"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """SUIIIII"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """SUIIIII"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """SUIIIII"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SUIIIII"""
    def __init__(self):
        """SUIIIII"""
        self.__head = None

    def sorted_insert(self, value):
        """SUIIIII"""
        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tempNode = self.__head
            while (tempNode.next_node is not None and
                    tempNode.next_node.data < value):
                tempNode = tempNode.next_node
            newNode.next_node = tempNode.next_node
            tempNode.next_node = newNode

    def __str__(self):
        """SUIIIII"""
        data_list = []
        node = self.__head
        while node is not None:
            data_list.append(str(node.data))
            node = node.next_node
        return ('\n'.join(data_list))
