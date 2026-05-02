class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        currSum=nums[0]
        n=len(nums)
        for i in range(1,n):
            num=nums[i]
            currSum=max(num,currSum+num)
            maxSum=max(currSum,maxSum)
        return maxSum


        