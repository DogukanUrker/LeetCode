class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del(nums1[m:])
        del(nums2[n:])
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
