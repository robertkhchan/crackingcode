'''Chapter 1| Arrays and Strings

Created on Mar 20, 2016

@author: Robert Chan
'''
import numpy as np

class ChapterOne(object):

    
    def __init__(self):
        pass
    

    def question1_mine(self, stringToVerify):
        '''Implement an algorithm to determine if a string has all unique characters. 
           What if you can not use additional data structures?
        '''
        isUnique = True
        
        sortedString = sorted(stringToVerify)
        for i in range(len(sortedString)-1):
            if (sortedString[i]==sortedString[i+1]):
                isUnique = False
                break
            
        return isUnique
    
    
    def question1(self, stringToVerify):
        return len(stringToVerify) == len(set(stringToVerify)) 
        
            
    def question2_mine(self, stringToReverse):
        '''Write code to reverse a String
        '''        
        stringToReverse = list(stringToReverse)
        
        indexHead = 0
        indexTail = len(stringToReverse)-1
        
        while (indexHead < indexTail):
            c = stringToReverse[indexHead]
            stringToReverse[indexHead] = stringToReverse[indexTail]
            stringToReverse[indexTail] = c
            indexHead += 1
            indexTail -= 1
            
        return str("".join(stringToReverse))
    
    
    def question2(self, stringToReverse):
        '''Write code to reverse a String
        '''
        return stringToReverse[::-1]
        
            
    def question3_mine(self, stringToProcess):
        '''Design an algorithm and write code to remove the duplicate characters 
           in a string without using any additional buffer. NOTE: One or two 
           additional variables are fine. An extra copy of the array is not.
        '''                    
        return "".join(sorted(set(stringToProcess)))
    
                
    def question3(self, stringToProcess):
        '''Design an algorithm and write code to remove the duplicate characters 
           in a string without using any additional buffer. NOTE: One or two 
           additional variables are fine. An extra copy of the array is not.
        '''
        from collections import OrderedDict
        return "".join(OrderedDict.fromkeys(stringToProcess))
    
    
    def question4(self, string1, string2):
        '''Write a method to decide if two strings are anagrams or not
        '''
        return set(string1) == set(string2)
    
    
    def question5(self, stringToProcess):
        '''Write a method to replace all spaces in a string with ‘%20’.
        '''
        return stringToProcess.replace(" ","%20")
    
    
    def question6(self, matrix):
        '''Given an image represented by an NxN matrix, where each pixel 
           in the image is 4 bytes, write a method to rotate the image by 
           90 degrees. Can you do this in place?
        '''
        m = np.array(matrix)
        m = np.rot90(m,3)        
        return m.tolist()
    
    
    def question7(self, matrix):
        '''Write an algorithm such that if an element in an MxN matrix is 0, 
           its entire row and column is set to 0.
        '''
        coordinates = []
        
        m = np.array(matrix)
        for (x,y), value in np.ndenumerate(m):
            if (value == 0):
                coordinates.append((x,y))
                
        for (x,y) in coordinates:
            m[x,:] = 0
            m[:,y] = 0
            
        return m.tolist()
    
    
    def question8(self, string1, string2):
        '''Assume you have a method isSubstring which checks if one word 
           is a substring of another. Given two strings, s1 and s2, write 
           code to check if s2 is a rotation of s1 using only one call to 
           isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
        '''
        def isSubstring(str1, str2):
            return str2.find(str1) >= 0
        
        result = False
        
        if (string1 == string2):
            return result
        
        indexSubstring = -1
        indexWordEnd = len(string1)
        while (indexWordEnd > 0):
            if (isSubstring(string1[0:indexWordEnd], string2)):
                indexSubstring = string2.find(string1[0:indexWordEnd])
                break;
            else:
                indexWordEnd -= 1
            
        if (indexSubstring != -1):
            end = len(string2)
            result = string1 == string2[indexSubstring:end]+string2[0:indexSubstring]  
        
        return result