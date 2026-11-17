# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             j = i+1
#             while j <len(nums):
#                 if nums[i] == nums[j]:
#                     return True
                    
#                 j += 1

        
#         return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):

            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
 

        
        return False