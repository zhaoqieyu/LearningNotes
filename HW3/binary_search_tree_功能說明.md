# Binary Search Tree_功能說明
>以作業的程式碼為例                      
 限制條件:                            
 1. 搜尋方式：preorder                          
 2. 修改/刪除 : 一樣的要一起處理                   
 3. 如何比較 : 小於等於 root：放左邊  /  大於 root：放右邊                    
 4. 限制 : 最終BST深度不能大於原深度

## 新增
>insert():在BST插入一數

* 分為兩種種況思考 :
   


      def insert(self, root, val):
          if val <= root.val :
              if root.left == None :
                 root.left = TreeNode(val)
                 return root.left
              else:
                 return self.insert(root.left,val)   
          elif val > root.val :
              if root.right == None :
                 root.right = TreeNode(val)
                 return root.right
              else:
                 return self.insert(root.right,val)


## 刪除
>delete ( ) : 在BST刪除此數(可能有多個)

                 
## 查詢
>search ( ) : 在BST找尋一數

* 何謂尋訪traversal??

* 分為三種狀況思考:                
  1.若要搜尋的值**等於**root，則**直接回傳**root
  2.若要搜尋的值**小於**root，則要往左邊搜尋                   
  3.若要搜尋的值**大於**root，則

      def search(self, root, target):
          if target == root.val :
             return root
          elif target < root.val :
             if root.left == None :
                return None
             else:
                return self.search(root.left,target)
          elif target > root.val :
             if root.right == None:
                return None
             else:
                return self.search(root.right,target)

## 修改
>modify ( ) : 在BST用新數取代舊數(可能有多個)

## reference
http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html

