class Solution(object):
    def findDuplicate(self, nums):
        check = set()
        for i in nums:
            if i in check:
                return i
            check.add(i)