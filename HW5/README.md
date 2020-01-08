# 何謂 Breadth-First Search(BFS)?
* 廣度優先搜尋
* 有兩個 Queue 做紀錄 ( 假設為state1、state2 ) ，再進行比對，其中 state1 可以想像成一個暫存的待完成清單， state2 可以想像成最終結果

# 何謂 Depth-First Search(DFS)?
* 深度優先搜尋
* push 的時候一次 push 完，pop的時候去最後一筆

# BFS & DFS 比較

內容  | BFS | DFS | 
 :---: | :---: | :---: |
作法 | queue | stack |
push | append(x) : 從下面加入 | append(x) : 從下面加入 | 
pop | pop(0) : 從最下面取出 | pop() : 從最上面取出 | 
小結 | 先進先出 | 後進先出 |
