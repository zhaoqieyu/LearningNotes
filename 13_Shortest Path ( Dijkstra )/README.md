# Shortest Path 
>最短路徑

## 原理
* 何謂路徑 : 在圖上任取兩點，分別作為起點和終點，可以規劃出許多條由起點到終點的路線，且這條路線不會來來回回繞圈子、不會重覆經過同一個點和同一條邊的路線
* 特性 :
    * 從起點到終點，**邊權重總和最小**的路徑
    * 可能有許多條，也可能不存在
    * 當起點到終點不通、不存在路徑的時候，則沒有最短路徑
    * **不見得是邊最少、點最少**的路徑
    * 邊 ( E ) = 點 ( V ) - 1
* 限制: 
  * 該路徑**有連通**
  * 該路徑**不能有circle**
  
## 使用的演算法 : Dijkstra演算法 ( 戴克斯特拉算法 )
>用來解決最短路徑問題 ( shortest path ) 的演算法

* 重要小規則:


* 做法 ( 見 HW6 流程圖 )

    Step1. 會先給定一張圖
             
    Step2. 
                         
    Step3. 
    
    Step4. 
    
    Step5. 
    
    Step6. 
    
## reference
http://www.csie.ntnu.edu.tw/~u91029/Path.html

https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95

http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html

https://en.wikipedia.org/wiki/Shortest_path_problem
