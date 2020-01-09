#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None     

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        answer = current = ListNode(0) #本來只有打current，想說回傳current，但結果顯示找不到，所以又另外設一個來回傳結果
        while head != None : #當有節點時
            if head.val != val: #走訪連結陣列，只要比對目前節點與val相等，就移除目前這點，當head不是val時
                #移除節點 : 讓前一個節點跳過目前節點直接指向下一個節點
                current.next = ListNode(head.val) #當前的節點有子節點
                current = current.next #把當前的節點改成它的下一個
            head = head.next #head改成head的下一筆
        return answer.next #回傳答案

#reference :　https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/203md.html
