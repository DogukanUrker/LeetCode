class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            match nums[i] in d:
                case True:
                    return [d[nums[i]],i]
                case False:
                    d[target-nums[i]] = i
