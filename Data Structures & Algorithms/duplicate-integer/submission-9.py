class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        num=sorted(nums)
        for i in range(n-1):
            if num[i]==num[i+1]:
                return True
        return False