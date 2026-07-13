class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            prod=1
            for j in range(n):
                if i==j:
                    continue
                prod*=nums[j]
            ans.append(prod)
        return ans