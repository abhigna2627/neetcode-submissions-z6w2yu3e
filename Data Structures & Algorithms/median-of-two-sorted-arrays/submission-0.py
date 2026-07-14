
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Merge the two arrays
        a = nums1 + nums2

        # Sort the merged array
        a.sort()

        # Middle index
        c = len(a) // 2

        # Even number of elements
        if len(a) % 2 == 0:
            return (a[c] + a[c - 1]) / 2

        # Odd number of elements
        else:
            return a[c]
               