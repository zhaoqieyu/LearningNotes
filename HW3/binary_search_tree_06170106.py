#!/usr/bin/env python
# coding: utf-8

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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
            
    def delete(self, root, target):
        dad = None
        node = root
 
        while node and node.val != target:
            dad = node
            if target < node.val:
                node = node.left
            elif target > node.val:
                node = node.right

        if node is None or node.val != target: 
            return root 

        elif node.left is None and node.right is None : 
            if target <= dad.val:
                dad.left = None
            else:
                dad.right = None
            return self.delete(root,target) 

    
        elif node.left != 0 and node.right is None: 
            if target <= dad.val:
                dad.left = node.left
            else:
                 dad.right = node.left
            return self.delete(root,target)
    
        elif node.left is None and  node.right != 0 :
            if target <= dad.val:
                dad.left = node.right
            else:
                dad.right = node.right
            return self.delete(root,target)      

        else: 
            delete_nodeparent = node
            delete_node = node.left
            while delete_node.right: 
                delete_nodeparent = delete_node            
                delete_node = delete_node.right

            node.val = delete_node.val 
            if delete_node.left == 0: 
                if delete_node.val < delete_nodeparent.val:
                    delete_nodeparent.right = None
                else:
                    delete_nodeparent.left = None
            elif delete_node.left != 0:  
                if delete_nodeparent.val > delete_node.val:
                    delete_nodeparent.right = delete_node.left
                else:
                    delete_nodeparent.left = delete_node.left
            return self.delete(root,target)
        
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
            
    def modify(self, root, target, new_val):
        FIND_NEXT = 2
        while self.delete_1(root,target) == FIND_NEXT :
            self.insert(root,new_val)
        root = self.delete_1(root,target)
        return root
 
    def delete_1(self, root, target):    
        FIND_NEXT=2
        dad = None
        node = root        
    
        while node and node.val != target:
            dad = node
            if target < node.val:
                node = node.left
            elif target > node.val:
                node = node.right

        if node is None or node.val != target: 
            return root
       
        elif node.left is None and node.right is None: 
            if target < dad.val:
                dad.left = None
            else:
                dad.right = None
            return FIND_NEXT 

        elif node.left != 0 and node.right is None: 
            if target < dad.val:
                dad.left = node.left
            else:
                dad.right = node.left
            return FIND_NEXT

        elif node.left is None and node.right != 0: 
            if target < dad.val:
                dad.left = node.right
            else:
                dad.right = node.right
            return FIND_NEXT

        else: 
            delete_nodedad = node
            delete_node = node.left
            while delete_node.left: 
                delete_nodedad = delete_node            
                delete_node = delete_node.right

            node.val = delete_node.val 
            if delete_node.left == 0: 
                if delete_node.val < delete_nodedad.val:
                    delete_nodedad.right = None
                else:
                    delete_nodedad.left = None
            elif delete_node.left != 0:  
                if delete_nodedad.val > delete_node.val:
                    delete_nodedad.right = delete_node.left
                else:
                    delete_nodedad.left = delete_node.left
            return FIND_NEXT
