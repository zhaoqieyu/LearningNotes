# Binary Search Tree_功能說明

## 新增
>insert():在BST插入一數
      
## 刪除
>delete ( ) : 在BST刪除此數(可能有多個)

分為三種種況思考 : 

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
## 查詢
>search ( ) : 在BST找尋一數

## 修改
>modify ( ) : 在BST用新數取代舊數(可能有多個)

## reference
