class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        num=sorted(nums)
        for i in range(n-1):
            if num[i]==num[i+1]:
                return True
        return False

'''seen=set()
        for num in nums:
            if num in seen:
                return True
            if num not in seen:
                seen.add(num)
        return False'''
