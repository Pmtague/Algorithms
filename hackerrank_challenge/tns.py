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
	arr.sort()
	print(arr)

	hash_table = {}

	new_list = []

	# for num in range(0, len(arr) - 2):
	# 	print("Num", arr[num])
	# 	for num2 in range(1, len(arr) - 1):
	# 		print("Num 2", arr[num2])
	# 		for num3 in range(2, len(arr)):
	# 			# print("Num 3", arr[num3])
	# 			print("Num Sum", arr[num] + arr[num2] + arr[num3])
	# 			if num + num2 + num3 == target:
	# 				list_one = [num, num2, num3]
	# 				list_one.sort()
	# 				print(list_one)
	while arr[-1] >= target:
		arr.pop()

	if arr[-1] < target:
		remainder = target - arr[-1]
	
	for num in arr:
		hash_table[num] = remainder - num
	
	for key in hash_table:
		if hash_table[key] in hash_table and hash_table[key] not in new_list:
			new_list.append([key, hash_table[key], arr[-1]])
	
	half_new_list = []

	for item in range(0, len(new_list) / 2):
		half_new_list.append(new_list[item])
		print(new_list)
	
	# for item in new_list:
	# 	item.sort()
	# 	print(new_list)
	
	# for index in range(0, len(new_list) - 2):
	# 	if new_list[index] == new_list[index + 1]:
	# 		new_list.pop(index)
	# 		print(new_list)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target = 30
threeNumberSum(array, target)