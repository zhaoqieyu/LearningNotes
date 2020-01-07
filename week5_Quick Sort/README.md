# Quick Sort
>快速排序法
## 基本觀念
快速排序法:對一段尚未排序的數列做排序，是普遍被認為最快的排序演算法!
## 做法
      Step1. 先找基準點
             → 此基準點可以隨意找(中間較佳)，但之後都要使用一致的規則
              ex:第一次比的時候找中間那筆，下一輪比的時候也要找中間那筆
              
      Step2. 分一半，從左到右的數字依序和此基準點(pivot)比大小 → 丟過去先不用排!!!
                 比基準點大放左邊
                 比基準點小放右邊
                 相等的隨便放就好
                 
     Step3. 第一輪比完後，再從左右兩堆分別找出基準點繼續筆下一輪
     
     Step4. 直到沒有數字可再進行切割時停止 → 當1/2的X次方 = 1的時候停下來
## reference
http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
