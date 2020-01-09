class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        a = {} 
        
        for i in range(len(nums)): 
            ok = target - nums[i] 
            if ok in a: 
                result0 = a[ok]
                result1 = i
                return [result0, result1]
            else: #若ok在a裡面
                a[nums[i]] = i 
