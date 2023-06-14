class Solution(object):
    def sortColors(self, nums):
        l = len(nums)
        nums += nums.count(0) * [0]
        nums += nums.count(1) * [1]
        nums += nums.count(2) * [2]
        del nums[0:l]