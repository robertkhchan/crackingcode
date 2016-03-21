'''
Created on Mar 20, 2016

@author: robert
'''
from unittest import TestCase
from chapter_one import ChapterOne

class TestChapterOne(TestCase):

    # Question 1
    def testQuestion1Mine_IsUnique(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1_mine("abcde")
        
        self.assertTrue(isUnique)
        
    def testQuestion1Mine_IsNotUnique(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1_mine("abcda")
        
        self.assertFalse(isUnique)
        
    def testQuestion1Mine_Empty(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1_mine("")
        
        self.assertTrue(isUnique)
        
    def testQuestion1_IsUnique(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1("abcde")
        
        self.assertTrue(isUnique)
        
    def testQuestion1_IsNotUnique(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1("abcda")
        
        self.assertFalse(isUnique)
        
    def testQuestion1_Empty(self):
        chapter1 = ChapterOne()
        isUnique = chapter1.question1("")
        
        self.assertTrue(isUnique)
        
        
    # Question 2
    def testQuestion2Mine_OddLength(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2_mine("abcde")
        
        self.assertEquals("edcba", reversedString)  

    def testQuestion2Mine_EvenLength(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2_mine("abcdef")
        
        self.assertEquals("fedcba", reversedString)
        
    def testQuestion2Mine_SingleCharacter(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2_mine("a")
        
        self.assertEquals("a", reversedString)
        
    def testQuestion2_OddLength(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2("abcde")
        
        self.assertEquals("edcba", reversedString)  

    def testQuestion2_EvenLength(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2("abcdef")
        
        self.assertEquals("fedcba", reversedString)
        
    def testQuestion2_SingleCharacter(self):
        chapter1 = ChapterOne()
        reversedString = chapter1.question2("a")
        
        self.assertEquals("a", reversedString)    

        
    # Question 3
    def testQuestion3Mine(self):
        chapter1 = ChapterOne()
        processedString = chapter1.question3_mine("singing")
        
        self.assertEquals("gins", processedString)  
        
    def testQuestion3(self):
        chapter1 = ChapterOne()
        processedString = chapter1.question3("singing")
        
        self.assertEquals("sing", processedString)  


    # Question 4
    def testQuestion4(self):
        chapter1 = ChapterOne()
        
        self.assertTrue(chapter1.question4("sing", "gins"))
        self.assertFalse(chapter1.question4("song", "gins"))  
        
        
    # Question 5
    def testQuestion5(self):
        chapter1 = ChapterOne()
        
        self.assertEquals("sing", chapter1.question5("sing"))  
        self.assertEquals("s%20i%20n%20g%20", chapter1.question5("s i n g "))
        self.assertEquals("s%20%20i", chapter1.question5("s  i"))  
        
        
    # Question 6
    def testQuestion6(self):
        chapter1 = ChapterOne()
        
        self.assertEquals(
            [[7,4,1],
             [8,5,2],
             [9,6,3]], 
                          
            chapter1.question6(
            [[1,2,3],
             [4,5,6],
             [7,8,9]]))  
        
            
    # Question 7
    def testQuestion7_middle(self):
        chapter1 = ChapterOne()
        
        self.assertEquals(
            [[1,0,3],
             [0,0,0],
             [7,0,9]], 
                          
            chapter1.question7(
            [[1,2,3],
             [4,0,6],
             [7,8,9]]))    
    
    def testQuestion7_corner(self):
        chapter1 = ChapterOne()
        
        self.assertEquals(
            [[1,2,0],
             [4,5,0],
             [0,0,0]], 
                          
            chapter1.question7(
            [[1,2,3],
             [4,5,6],
             [7,8,0]]))  
        
    def testQuestion7_multiple(self):
        chapter1 = ChapterOne()
        
        self.assertEquals(
            [[ 1, 0, 3, 4, 0],
             [ 0, 0, 0, 0, 0],
             [11, 0,13,14, 0],
             [ 0, 0, 0, 0, 0]], 
                          
            chapter1.question7(
            [[ 1, 2, 3, 4, 5],
             [ 6, 0, 8, 9,10],
             [11,12,13,14,15],
             [16,17,18,19, 0]]))  
                
                
    
    def testQuestion8(self):
        chapter1 = ChapterOne()
        
        self.assertTrue(chapter1.question8("erbottlewat","waterbottle"))  
        self.assertFalse(chapter1.question8("erbottleaaa","waterbottle"))  
        self.assertFalse(chapter1.question8("waterbottle","waterbottle"))  
        
        self.assertFalse(chapter1.question8("abcde","ghijk"))  
        self.assertTrue(chapter1.question8("abcde","eabcd"))
        self.assertTrue(chapter1.question8("abcde","deabc"))
        self.assertTrue(chapter1.question8("abcde","cdeab"))
        self.assertTrue(chapter1.question8("abcde","bcdea"))
                