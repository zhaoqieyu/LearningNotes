#!/usr/bin/env python
# coding: utf-8

# # HW1_QuickSort(1018)
# 06170106趙緁愉
# 
# ##基本觀念
# 快速排序法:對一段尚未排序的數列做排序，是普遍被認為最快的排序演算法!
#   * STEP1 先找基準點
#           → 此基準點可以隨意找(中間較佳)，但之後都要使用一致的規則
#            ex:第一次比的時候找中間那筆，下一輪比的時候也要找中間那筆
#   * STEP2 從左到右的數字依序和此基準點(pivot)比大小
#             比基準點大放左邊
#             比基準點小放右邊
#             相等的隨便放就好
#   * STEP3 第一輪比完後，再從左右兩堆分別找出基準點繼續比較
#   * STEP4 直到沒有數字可再進行切割時停止
#   
# ##實際演練
# ★EX:9,6,4,7,8,3,8
#   * 由於丟到左右兩堆的數字先不用排序，故最終使用「append」的方式直接加到該堆最後面較方便

# In[6]:


Example = [9,6,4,7,8,3,8] 

def quicksort(Example):
    if len(Example)<=1:   #若這串數列中的元素<=1，則不用排序，直接回傳一樣的數列即可
        return Example
    
    else:                 #否則，建立下列list
        
        pivot = Example[len(Example)//2-1]   #基準點找中間值
        
        #把整串數列分成三部分 → 設三個list，以便之後把和基準點比完大小的數丟入
        left_smaller=[]   #左一個(較小)
        pivot_equal=[]    #基準點一個(相等)
        right_bigger=[]   #右一個(較大)
     
    
    for i in Example:
        if i < pivot:
            left_smaller.append(i)        #若該數小於基準點，放右邊
        elif i == pivot:
            pivot_equal.append(i)         #若該數等於基準點，加到基準點的後面
        else:
            right_bigger.append(i)        #其餘(也就是大於基準點)，放左邊
            
    return quicksort(left_smaller) + pivot_equal + quicksort(right_bigger)   #排完時，從左到右依序把各個list串聯

quicksort(Example)


# ##問題與學習
#   * 一開始只想到**大於和小於**，但因為我設定的數列剛好是有相同的值，結果就一直跑不出來 → 發現**等於**也要考慮
#   * 後來參考其他寫法，發現我還漏掉了如果一開始的數列**只有一筆資料**的情況!!!，因為很直觀的想說要比大小，那一定是要有很多數字互相比較
#       → 只有一筆其實**不用再做比較**
#   * 程式碼要有意義 : 用到再寫

# ##參考資料
# (http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)

# In[ ]:





# In[ ]:




