class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        current_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if current_index != i:
                    nums[current_index], nums[i] = nums[i], nums[current_index]
                current_index += 1
            
#reference : https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/283md.html
