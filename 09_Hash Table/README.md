# Hash 原理解釋
>所有資料結構中應用最廣泛的

雜湊(Hash)算法一種用在資料編碼中的技術，最主要分為雜湊函數（Hash Function）和雜湊表（Hash Table）兩個部份

## Hash Function 
>雜湊函數

> 類似於**一台轉換器**，丟輸入進去就會產生一個輸出

**透過編碼規則，將所有字串可以轉成單一編號(唯一值)** ，也就是說將**輸入的資料(key)，透過一樣的規則**固定資料的格式，使得資料量變小，**輸出**的值稱為**雜湊值（hash values)**

* 特性
  * 運算速度快
  * 不可逆性 : 轉換時有一個很重要的特性就是**單向**，輸入值可以經由轉換得到輸出值，但輸出值卻不可得到輸入值，因此**無法從雜湊值推回原本的資料是什麼** 
  * 根據同一函式，輸入不同的資料，不可能得到相同的輸出，也就是說如果兩個雜湊值是不相同的，兩個輸入值也不相同
  * 根據同一函式，輸入不同的資料，可能得到相同的輸出，也就是說如果兩個雜湊值相同，兩個輸入值可能相同、也可能不同，此狀況稱為**雜湊碰撞（collision）** 
  
## Hash Table
>雜湊表
>雜湊函式的一個主要應用

## 舉例(以下圖為例)
**把Table想像成「書桌」、  buckets想像成書桌的「抽屜」**

為了要能更快速找到物品，希望能夠「每一個抽屜只放一個物品」

只要拿著Key，再透過中間的hash function就可以找到對應的抽屜(指出東西放在「第幾個」抽屜，即抽屜的index)，並能夠同時保證此抽屜內的東西是Key所要找的物品

但如果「同一個抽屜裡有兩個以上的物品」時，便有可能找錯物品，就要再透過「linked list」的方法往後尋找

ex : 此觀念類似於我國的**身分證字號**，每個人都有屬於自己的號碼，即使是同名同姓的人也不例外，方便搜尋及管理，
![hash table](https://miro.medium.com/max/2000/1*78wQr8-2tEPKWa0iobs8QQ.png)
圖片來源 :　https://medium.com/php-hacks/manipulating-zend-hash-1-a87906bc6e9c
## reference
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8

https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view
