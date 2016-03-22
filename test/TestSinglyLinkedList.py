'''
Created on Mar 21, 2016

@author: robert
'''
from unittest.case import TestCase
from datatype.SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(TestCase):


    def testAdd(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        
        self.assertEqual(5, mylist.node.value)

    def testRemove(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        mylist.add(7)
        
        self.assertFalse(mylist.node.next is None)
        self.assertEqual(6, mylist.node.next.value)
        
        mylist.remove(SinglyLinkedList.Node(6))
        
        self.assertFalse(mylist.node.next is None)
        self.assertEqual(7, mylist.node.next.value)
        
        
    def testRemoveLastElement(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        
        self.assertFalse(mylist.node.next is None)
        self.assertEqual(6, mylist.node.next.value)
        
        mylist.remove(SinglyLinkedList.Node(6))
        
        self.assertTrue(mylist.node.next is None)
        
    
    def testFind(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        mylist.add(7)
        
        foundNode = mylist.find(6)
        
        self.assertFalse(foundNode is None)
        self.assertEqual(6, foundNode.value)
        self.assertEqual(7, foundNode.next.value)
        
    def testFindThenRemove(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        mylist.add(7)
        
        foundNode = mylist.find(6)
        mylist.remove(foundNode)
        
        self.assertEqual(5, mylist.node.value)
        self.assertEqual(7, mylist.node.next.value)
        
        foundNode = mylist.find(5)
        mylist.remove(foundNode)
        
        self.assertEqual(7, mylist.node.value)
        self.assertTrue(mylist.node.next is None)
        
        
    def testGet(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        mylist.add(7)
        
        foundNode = mylist.get(1)
        
        self.assertFalse(foundNode is None)
        self.assertEqual(6, foundNode.value)
        self.assertEqual(7, foundNode.next.value)

    def testGetThenRemove(self):
        mylist = SinglyLinkedList()
        mylist.add(5)
        mylist.add(6)
        mylist.add(7)
        
        foundNode = mylist.get(0)
        mylist.remove(foundNode)
        
        self.assertEqual(6, mylist.node.value)
        self.assertEqual(7, mylist.node.next.value)
        
        foundNode = mylist.get(1)
        mylist.remove(foundNode)
        
        self.assertEqual(6, mylist.node.value)
        self.assertTrue(mylist.node.next is None)