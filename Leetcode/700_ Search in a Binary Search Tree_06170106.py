# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while not root: #若該節點不存在
            return None #直接回傳None
        if root.val == val: #若樹根的節點剛好等於要找的值
            return root #則直接回傳樹根
        elif root.val > val : #若樹根的節點大於等於要找的值
            return self.searchBST(root.left, val) #往左子樹中找
        elif root.val < val:  #若樹根的節點小於等於要找的值
            return self.searchBST(root.right, val) #往右子樹中找

#reference : https://blog.csdn.net/fuxuemingzhu/article/details/81015754
