# Linked List
>連結串列

## 基本觀念
* 資料結構的一種，使用一個節點 ( node ) 來存取資料，並利用每個node中的pointer指向下一個node，把多個 node 和 pointer 串在一起就是一個Linked List，而Linked list的終點以NULL來代表 ( 如下圖所示 )

![Linked List](https://github.com/zhaoqieyu/LearningNotes/blob/master/pictures/LinkedList.jpg?raw=true)

* 優點 : 新增/刪除資料較簡單
* 缺點 : 因為Linked list沒有index，若要找到特定node，需要從頭開始找起，搜尋的時間複雜度為O(N)


## 功能-新增、刪除、搜尋 : 調整pointer即可
有兩種狀況:
* node在開頭 : 新增、刪除只要 O ( 1 )
* 特定node : 在新增、刪除前要先執行 O ( N ) 的「搜尋」

## 語法:
* get(index) : 取得該index中的值
* addAtHead(val) : 把要新增的值放到 Linked List 的開頭
* addAtTail(val) : 把要新增的值放到 Linked List 的尾端
* addAtIndex(index, val) : 把要新增的值放到 Linked List 指定的 index 上，如果 :
  * index > Linked List 的長度 : 代表該 index 不存在，故不變
  * index < 0 : 直接加在開頭
  * index = Linked List 的長度 : 直接加在尾端
* deleteAtIndex(index) : 刪掉指定 index 位置上的值
## reference
http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html
