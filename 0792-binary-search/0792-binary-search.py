class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + r
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target: 
                r = m - 1
            else:
                return m
        return -1