class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        product = math.prod(nums)
        new = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new.append(product//nums[i])
            else:
                numss = nums.copy()
                numss.pop(i)
                a = math.prod(numss)
                new.append(a)
        return(new)