#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):

    node1 = head1
    node2 = head2

    d1 = set([])
    d2 = set([])

    while (node1 != None or node2 != None):
        if node1:
            d1.add(node1)
        if node1.next:
            d1.add(node1.next)
            node1 = node1.next
            if node1.next:
                d1.add(node1.next)
                node1 = node1.next
        if node2:
            d2.add(node2)
        if node2.next:
            d2.add(node2.next)
            node2 = node2.next

        for i in d2:
            if i in d1:
                return i.data


if __name__ == '__main__':
