'''
Created on Mar 21, 2016

@author: robert
'''
from unittest import TestCase
from datatype.BinarySearchTree import BinarySearchTree


class Test(TestCase):


    def testAdd(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(6)
        tree.add(4)

        self.assertEqual(5, tree.node.value)
        self.assertEqual(3, tree.node.left.value)
        self.assertEqual(6, tree.node.right.value)
        self.assertEqual(4, tree.node.left.right.value)
        
        
    def testGetInOrder(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(6)
        tree.add(4)

        inOrderList = tree.getInOrder()
        
        self.assertEqual([3,4,5,6], inOrderList)
        
        
    def testGetPreOrder(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(6)
        tree.add(4)

        preOrderList = tree.getPreOrder()
        
        self.assertEqual([5,3,4,6], preOrderList)
        
        
    def testGetPostOrder(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(6)
        tree.add(4)

        postOrderList = tree.getPostOrder()
        
        self.assertEqual([4,3,6,5], postOrderList)
            
