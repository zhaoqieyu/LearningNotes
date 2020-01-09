class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= 0
        for j in range(len(nums)):
            if nums[j] != val :
                nums[i]= nums[j]
                i += 1
        return (i)
    
 #reference : https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/27md.html
