class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        match target in nums:
            case True:
                return nums.index(target)
            case _:
                for i in range(len(nums)):
                    if nums[i] > target:
                        return i 
                return len(nums)  

    
        
            

              
            
        