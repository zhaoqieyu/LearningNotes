# Heap sort
* linked list的變形
* tree的special case
* EX:堆杯子

## 基本觀念
* **每個node只能有兩個子節點** 
* **樹根(root)一定最小或最大**
* 先左後右
* 型態: 
    * 最小堆積(min heap) : 父節點的值小於子節點  `樹根(root)一定是最小值`
    * 最大堆積(max heap) : 父節點的值大於子節點  `樹根(root)一定是最大值`
      
## 做法
      Step1. build heap
             把數列建成一個heap → 無條件擺進heap
             
      Step2. transfer to min/max heap 
             再把heap轉換成max heap或min heap
             
      Step3. remove the node
      
      Step4. 從heap中依序抽出來（確保每一段都是heap) → 得到heap sort
>一個要花logn的時間 → 則n個的話共要花nlogn的時間
