def maxSubArray(self, nums: List[int]) -> int:
        cs=nums[0]
        os=nums[0]
        for i in range(1,len(nums)):
            if cs+nums[i]>nums[i]:
                cs+=nums[i]
            else:
                os=nums[i]
            os=max(cs,os)
            return os        
        
