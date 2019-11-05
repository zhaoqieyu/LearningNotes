# Merge sort
>合併排序法

## 基本觀念
* 指的是將兩個已排序的陣列合併成一個陣列
* 主要分成兩個步驟
    * 分割 : 透過遞迴把目前陣列**分割成兩半**
    * 整合 : **將上一步得到的子陣列合併**
      
## 做法
   >假設有7個數，由小到大排序，如連結中的流程圖所示
   
    Step1. 將陣列平均分堆，直到只剩下一個元素
             
    Step2. 兩兩合併，同時進行排序
           → HOW?? 假設今天有兩個子陣列left、right，要把它們排序並合併成一個新的陣列new
                   則new的第0筆資料 : left和right的第0筆較小者(left)
                   而new的第1筆資料 : left的下一筆資料(第1筆)和right的第0筆資料較小者                
                         
    Step3. 重複上步驟，直到合併成一個完整的陣列 
   
## reference
###### [🔗流程圖](https://github.com/zhaoqieyu/LearningNotes/blob/master/pictures/merge_sort_%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)
