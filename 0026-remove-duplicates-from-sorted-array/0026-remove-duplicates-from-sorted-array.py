class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        match len(nums) == 0:
            case True:
                return 0
            case False:
                ans = 1
                for i in range(1, len(nums)):
                    match nums[i] != nums[i-1]:
                        case True:
                            nums[ans] = nums[i]
                            ans += 1
                return ans