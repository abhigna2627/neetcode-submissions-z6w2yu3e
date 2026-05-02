class Solution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key in freq:
            if freq[key] > len(nums) // 2:
                return key

        return nums[0]   # fallback (guarantee exists)