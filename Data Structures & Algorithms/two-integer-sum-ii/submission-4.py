class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        ans=[]
        summ=0
        for i in range(len(numbers)):
            summ=numbers[l]+numbers[r]

            if summ==target:
                ans=[l+1,r+1]
            if summ>target:
                r-=1
            if summ<target:
                l+=1
        return ans
        