'''
Created on Mar 21, 2016

@author: robert
'''

class SinglyLinkedList(object):
    '''
    classdocs
    '''
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None
            
        def getNext(self):
            return self.next
            
        def setNext(self, node):
            self.next = node   

        def hasNext(self):
            return self.next != None


    def __init__(self):
        '''
        Constructor
        '''
        self.node = None
        
    def add(self, value):
        if (self.node == None):
            self.node = SinglyLinkedList.Node(value)
        else:
            lastNode = self.node
            while (lastNode.hasNext()):
                lastNode = lastNode.getNext()
                
            lastNode.setNext(SinglyLinkedList.Node(value))
    
    def remove(self, node):
        if (node == None): raise RuntimeError("Cannot remove null object")
        
        tmp = node.next
        if (tmp != None):
            # if node is not last, copy next node's value and remove next node 
            node.value = tmp.value
            node.next = tmp.next
        else:
            # if node is last, find the previous node and set next node to null
            tmp = self.node
            previousNode = None
            nextNode = None
            while (tmp != None):
                if (node.value != tmp.value):
                    previousNode = tmp
                    tmp = tmp.next
                else:
                    nextNode = tmp.next
                    break;
                
            if (previousNode != None):
                previousNode.next = nextNode
                node = None
                
        
    def find(self, value):
        foundNode = None
        
        tmp = self.node
        while(tmp != None):
            if (tmp.value != value):
                tmp = tmp.next
            else:
                foundNode = tmp
                break
            
        return foundNode
    
    def get(self, index):
        if (index < 0): raise RuntimeError("index cannot be less than 0")
        
        foundNode = self.node
        
        while (index > 0):
            foundNode = foundNode.next
            index -= 1
            
        return foundNode
        