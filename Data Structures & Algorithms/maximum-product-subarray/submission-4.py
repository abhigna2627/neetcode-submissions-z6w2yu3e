class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax=nums[0]
        currMin=nums[0]
        maxProd=nums[0]
        n=len(nums)
        for i in range(1,n):
            num=nums[i]
            if (num<0):
                currMax,currMin=currMin,currMax
            currMax=max(num,num*currMax)
            currMin=min(num,num*currMin)
            
            maxProd=max(currMax,maxProd)
        return maxProd