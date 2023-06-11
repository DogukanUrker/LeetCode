class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted((nums1 + nums2))
        i = (len(arr) - 1)/2
        if len(arr) % 2 == 1:
            return arr[int(i)]
        return (arr[int(i)]+arr[int(ceil(i))]) / 2


