class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for numero in nums2:
            nums1.append(numero)

        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        else:
            return nums1[len(nums1) // 2]
