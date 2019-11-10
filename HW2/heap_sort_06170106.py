#!/usr/bin/env python
# coding: utf-8

# In[1]:


#程式碼的解釋在學習歷程中的最終解

class Solution(object):
    list = []
    maxOrmin = "max" 
    changeEnd = 0  
    
    def Heapify(self, currentIndex): 

        left_child_Index = self.LeftChildIndex(currentIndex) 
        right_child_Index = self.RightChildIndex(currentIndex) 
        maxIndex = currentIndex 
        
        maxIndex = self.CompareResult(maxIndex, left_child_Index)
        maxIndex = self.CompareResult(maxIndex, right_child_Index)
        
        if maxIndex != currentIndex:  
            self.Change(currentIndex, maxIndex) 
            return self.Heapify(maxIndex) 

    def heap_sort(self,list):
        self.list=list
        rootIndex = 0 
        endIndex = len(self.list) 
        startIndex = endIndex // 2 - 1 

        for index in range(startIndex, -1, -1): 
            self.changeEnd = endIndex
            self.Heapify(index)
        
        for index in range(endIndex-1, 0, -1): 
            self.changeEnd = index
            self.Change(index, rootIndex)
            self.Heapify(rootIndex)
        return self.list
    
    def LeftChildIndex(self, parent_Index):
        return 2*parent_Index + 1 

    def RightChildIndex(self, parent_Index):
        return 2*parent_Index + 2 
            
    def Change(self, i, j): 
        self.list[j], self.list[i] = self.list[i], self.list[j] 

    def Compare(self, first_Index, second_Index): 
        if(self.maxOrmin == "max"):
            return self.list[first_Index] < self.list[second_Index]
        elif(self.maxOrmin == "min"):
            return self.list[first_Index] > self.list[second_Index]
    
    def IsExistIndex(self, index): 
        return index < self.changeEnd

    def CompareResult(self, maxIndex, compareIndex):
        if self.IsExistIndex(compareIndex) and self.Compare(maxIndex, compareIndex): 
            maxIndex = compareIndex
        return maxIndex


list = [9,6,21,19,23,8,6]

output = Solution().heap_sort(list)
output

