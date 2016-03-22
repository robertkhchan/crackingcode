'''
Created on Mar 21, 2016

@author: robert
'''
class BinarySearchTree(object):
    '''
    classdocs
    '''
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            
        def add(self, node):
            if (self.value > node.value):
                if (self.left is None):
                    self.left = node
                else:
                    self.left.add(node)
            elif (self.value < node.value):
                if (self.right is None):
                    self.right = node
                else:
                    self.right.add(node)            
        
        def setLeft(self, node):
            self.left = node
            
        def getLeft(self):
            return self.left
            
        def setRight(self, node):
            self.right = node
            
        def getRight(self):
            return self.right


    def __init__(self):
        '''
        Constructor
        '''
        self.node = None
        
        
    def add(self, value):
        newNode = BinarySearchTree.Node(value)
        if (self.node is None):
            self.node = newNode
        else:
            self.node.add(newNode)
            
            
    def getInOrder(self):
        return self.inOrderTraversal(self.node)    
    
    def inOrderTraversal(self, node):
        result = []
        
        if (node is None):
            return result
        
        if (node.left is not None):
            result = result + self.inOrderTraversal(node.left)
            
        result.append(node.value)
        
        if (node.right is not None):
            result = result + self.inOrderTraversal(node.right)
        
        return result
    
    
    def getPreOrder(self):
        return self.preOrderTraversal(self.node)
    
    def preOrderTraversal(self, node):
        result = []
        
        if (node is None):
            return result
        
        result.append(node.value)
        
        if (node.left is not None):
            result = result + self.preOrderTraversal(node.left)
        
        if (node.right is not None):
            result = result + self.preOrderTraversal(node.right)
        
        return result
    
    
    def getPostOrder(self):
        return self.postOrderTraversal(self.node)
    
    def postOrderTraversal(self, node):
        result = []
        
        if (node is None):
            return result
        
        if (node.left is not None):
            result = result + self.postOrderTraversal(node.left)
        
        if (node.right is not None):
            result = result + self.postOrderTraversal(node.right)

        result.append(node.value)
        
        return result

        
        
        
    