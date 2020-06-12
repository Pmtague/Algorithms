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



#
# Complete the 'removeKthLinkedListNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def threeNumberSum(arr, target):
    # Loop through the numbers in the array and add them to a hash table
    # Integer as key, remainder as value (target - key)
    # Loop through the hashtable values
        # if target - hashtable[key] 
    
    # Naive
	arr.sort(reverse=True)
	print(arr)

	hash_table = {}

	result = []

	for index in range(0, len(arr)-1):
		hash_table[arr[index]] = target - arr[index]
		print(hash_table)
	
	for key in hash_table:
		for index in range(0, len(arr)-1):
			difference = hash_table[key] - arr[index]
			if difference in hash_table and hash_table[key] in arr:
				new_result = [hash_table[key], arr[index], difference]
				new_result.sort()
				if new_result not in result:
					result.append(new_result)
					result.sort()
					print("Result", result)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target = 30
threeNumberSum(array, target)