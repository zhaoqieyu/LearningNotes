# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        while not root: ##若該節點不存在
            return TreeNode(val) #直接回傳
        if root.val > val: #若樹根的節點大於要找的值
            root.left = self.insertIntoBST(root.left, val) #則插入左子樹中
        elif root.val < val: #若樹根的節點小於等於要找的值
            root.right = self.insertIntoBST(root.right, val) #則插入右子樹中
        return root

#reference : https://blog.csdn.net/fuxuemingzhu/article/details/82385503 
