# Breadth-First Search(BFS)
>廣度優先搜尋

## 原理
>一層做完再往下做一層
* 有兩個 Queue 做紀錄 ( state1、state2 ) ，再進行比對，其中 **state1** 可以想像成一個暫存的**待完成清單**， **state2** 可以想像成**最終結果**
* 尋訪順序 : 
   * 從圖的出發點或某一節點 ( vertex , node ) 開始訪問 ( visiting ) ，先去最近一層的點
   * 走訪此節點所有相鄰且未拜訪過的節點
   * 由走訪過的節點繼續進行搜尋，走完這層，才去下一層
   * 直到所有點走完

* 實作：
  * 起點加入queue
  * 當queue沒有清空，則：從queue取出一點並送出，將其相鄰點中，還未曾加入queue過的，加入queue
  * 直到queue清完時，則結束

# Depth-First Search(DFS)
>深度優先搜尋

## 原理
>追根就柢 → 先遇到的節點先訪問，並且以先遇到的節點作為新的搜尋起點，直到所有有和edge相連的節點都被探索過
* 尋訪順序 :
  * 從圖的出發點或某一節點 ( vertex , node ) 開始訪問 ( visiting )，每一步依序想辦法走到最遠
  * 到達最遠後：
    * 若沒有路，才依序原路返回上一層
    * 若可以再有其他路走更深，往更深的路走

* 實作：
  * 起點加入stack
  * 當stack沒有清空，則：從stack取出一點並送出，將其相鄰點中，還未曾加入stack過的，加入stack
  * 直到stack清完時，則結束

# BFS & DFS 比較

內容  | BFS | DFS | 
 :---: | :---: | :---: |
作法 | queue | stack |
push | append(x) : 從下面加入 | append(x) : 從下面加入 | 
pop | pop(0) : 從最下面取出 | pop() : 從最上面取出 | 
小結 | 先進先出 | 後進先出 | 

## reference
https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2

https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
