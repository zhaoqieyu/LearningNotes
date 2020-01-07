# Stack
>堆疊

**後進先出**
* 類似編輯器中用的回到上一步的概念

* 可以想像成「盤子」
      
* 可以解謎宮的問題
	* 做法
	
      		Step1. 把要走的每一步丟到stack
             
     		Step2. 用push記錄每一步
		      	 → 因為存的時候就具備從最上面取的特性	
		       
			Step3. 故碰壁的時候(要上一步的時候)用一步一步退回去top
	
* 語法 :
	* `push()`    : 將資料加進去 Stack -----把盤子放到桌上
	* `pop(0)`     : 把最上面的數字取出來-----取出盤子(從最上面取)
	* `top()`     : 回傳最上面的資料-----告訴使用者最上面長怎樣，但沒被拿走
	* `isempty()` : 確認 Stack 裡面是否有資料-----有沒有盤子
	* `getsize()` : 回傳資料筆數-----有幾個盤子

# Queue
>佇列

**先進先出**
* 解決排程的需求 
  >一次只能解決一個問題，還沒被排到的放在queue 
     **EX:印表機**
* 可以想像成「排隊」
  >第一個到的先出去，不能插隊，只能從尾巴差資料

* 語法 : 
 	* `push()`           : 將資料加進去 Queue ，並更新成新的 Back
	* `pop()、dequeue()` : 把 Front 所指向的資料從 Queue 中移除，並更新 Front
	* `getFront()`       : 回傳 Front 所指向的資料
 	* `getBack()`        : 回傳 Back 所指向的資料
	* `isempty()`        : 確認 Queue 裡面是否有資料-----有沒有人在排隊
	* `getsize()`        : 回傳資料筆數-----幾個人在排隊

# reference
http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html
https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html


