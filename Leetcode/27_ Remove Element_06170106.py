class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= 0
        for j in range(len(nums)): #在num的長度內，所有的值
            if nums[j] != val : #若nums的第某項=目標值
                nums[i]= nums[j] # 則把當前這項的值改成nums[j]
                i += 1 #i也慢慢遞增
        return (i)
    
 #reference : https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/27md.html
