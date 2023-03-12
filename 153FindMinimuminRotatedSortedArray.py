class Solution:
    def findMin(self, nums: List[int]) -> int:

        # log n == binary
        # divid the nums into half and compare and then divid again until one is less 
        l = 0
        r = len(nums)-1
        
        
        res = nums[0]
        while l<= r:
            if nums[l]<nums[r]:
                res = min(res, nums[l])
            m = (l+r)//2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1 
        return res
