import math

class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, node, data):
        if self.root == None:
            self.root = Node(data)
            return node
        else:
            if data < node.data and node.left_child == None:
                node.left_child = Node(data)
            elif data < node.data:
                node.left_child = self.insert(node.left_child, data)
            elif data > node.data and node.right_child == None:
                node.right_child = Node(data)
            elif data > node.data:
                node.right_child = self.insert(node.right_child, data)

            return node

    def pre_order_traversal(self, node):
        if node:
            print("++++++++++++++++++")
            print(" root: ", node.data)
            print(" left: ", node.left_child.data if node.left_child else '-')
            print("right: ", node.right_child.data if node.right_child else '-')
            print("++++++++++++++++++")

            if node.left_child:
                self.pre_order_traversal(node.left_child)
            if node.right_child:
                self.pre_order_traversal(node.right_child)
    
    def in_order_feed(self, node):
        if node:
            arr = []
            if node.left_child:
                arr.append(**self.in_order_feed(node.left_child))
            arr.append(node.data)
            if node.right_child:
                arr.append(**self.in_order_feed(node.right_child))
            return arr

    def empty_tree(self, node):
        if node:
            if node.left_child:
                self.empty_tree(node.left_child)
                node.left_child = None
            if node.right_child:
                self.empty_tree(node.right_child)
                node.right_child = None
        self.root = None
    
    def build_tree_from_list(self, arr):
        if len(arr) <= 1:
            self.insert(self.root, arr[0])
        else:
            mid = len(arr) // 2
            self.insert(self.root, arr[mid])
            self.build_tree_from_list(arr[:mid])
            self.build_tree_from_list(arr[mid+1:])
    
    def balance(self):
        arr = self.in_order_feed(self.root)
        self.empty_tree(self.root)
        self.build_tree_from_list(arr)


bst = BinarySearchTree()
bst.insert(bst.root, 5)
bst.insert(bst.root, 10)
bst.insert(bst.root, 15)
bst.insert(bst.root, 20)
bst.insert(bst.root, 25)
bst.insert(bst.root, 30)
bst.insert(bst.root, 35)
bst.insert(bst.root, 40)

print('><><><><><><><><><><><><><><')
print("PREORDER")
print('><><><><><><><><><><><><><><')
bst.pre_order_traversal(bst.root)

bst.balance()
print('><><><><><><><><><><><><><><')
print("BALANCED")
print('><><><><><><><><><><><><><><')
bst.pre_order_traversal(bst.root)
