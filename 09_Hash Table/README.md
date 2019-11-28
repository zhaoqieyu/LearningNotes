# Hash Table
>雜湊表、哈希表


# Hash Function 
>雜湊函數

## 舉例(以下圖為例)
**把Table想像成「書桌」、  buckets想像成書桌的「抽屜」**

為了要能更快速找到物品，希望能夠「每一個抽屜只放一個物品」

只要拿著Key，再透過中間的hash function就可以找到對應的抽屜(指出東西放在「第幾個」抽屜，也就是抽屜的index)，並能夠同時保證此抽屜內的東西是Key所要找的物品

但如果「同一個抽屜裡有兩個以上的物品」時，便有可能找錯物品，就要再透過「linked list」的方法往後尋找

ex : 此觀念類似於我國的**身分證字號**，每個人都有屬於自己的號碼，即使是同名同姓的人也不例外
![hash table](https://miro.medium.com/max/2000/1*78wQr8-2tEPKWa0iobs8QQ.png)
圖片來源 :　https://medium.com/php-hacks/manipulating-zend-hash-1-a87906bc6e9c
## reference
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
