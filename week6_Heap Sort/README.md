# Heap sort
>堆積排序法
* linked list的變形
* tree的special case
* EX:堆杯子

## 基本觀念
* **每個節點(node)只能有兩個子節點** 
* **樹根(root)一定最小或最大**
* 型態 : 
    * 最小堆積(min heap) : 父節點的值小於子節點  `樹根(root)一定是最小值`
    * 最大堆積(max heap) : 父節點的值大於子節點  `樹根(root)一定是最大值`
* 節點生成順序 : **由上往下**、**由左往右**依次生成
* 如何建立heap?? **以max_heap為例**
    * (法一)每次將每個元素插入之後，邊做向上調整
    * (法二)一次讀入所有的元素放入陣列，從最後一個元素開始對其做向上調整
* 如何調整?? **以max_heap為例**
    * (法一)**向上調整** : 將一個節點與他的父節點比較，如果大於父節點便與其交換，利用遞迴一直往上做上述判斷，直到大於其父節點或是已換成root為止 
    * (法二)**向下調整** : 與其較大的子節點比較，如果小於較大的子節點，便與其交換，同樣使用遞迴，往下確認直到該節點皆小於其子節點為止
 * **一個要花logn的時間 → 則n個的話共要花nlogn的時間**
      
## 做法
   >假設有7個數，從i=0，如連結中的流程圖所示
    
    Step1. build heap 把數列建成一個heap 
           → HOW?? 把i=0,i=1,i=2...i=n+1 由上至下、左至右無條件擺進heap
             
    Step2. transfer to min/max heap 再把heap轉換成max heap或min heap
           → HOW?? 利用index找出父節點下面的兩個子節點進行比較(公式 :　l = 2*i+1、r = 2*i+2)
                   p.s.比較完一層再比下一層，一樣由左至右
                         
    Step3. remove the node 移除最上面的節點
    
    Step4. 把最後一個數字(heap中最後一層的最右邊的數字)拉到最上面的節點繼續進行比較
                             
    Step5. 把移除的node，從heap中依序抽出來
           → HOW?? 
             第一輪 : i=0(要移除的node)和i=6換位子(最後一個數字拉到最上面)，故移除的node會從最後往前依序排列，排在最後
             第二輪 : i=0(要移除的node)和i=5換位子(最後一個數字拉到最上面)，故移除的node會從最後往前依序排列，排在倒數第二(i=6前) 
             之後以此類推，得到heap sort
     
## reference
http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php

https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html
