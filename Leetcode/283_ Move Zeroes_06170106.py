class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        current_index = 0 #使用另外一個變數index來記錄碰到的非0數字
        for i in range(len(nums)):
            if nums[i] != 0: #遇到非0整數
                if current_index != i: #且非index
                    nums[current_index], nums[i] = nums[i], nums[current_index] #將整數塞到index的位子， 最後陣列長度扣除index就是0的數目，將陣列index之後的數字改為0就完成搬移的動作
                current_index += 1 #current_index遞增，去判斷下一個
            
#reference : https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/283md.html
