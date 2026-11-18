class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        dif = []
        for i in range(1,len(nums),1):
            dif.append(nums[i]-nums[i-1])
            # print(dif)
        max_count = 0
        cur_count = 0
        for num in dif:
            if num == 1:
                cur_count += 1
                if cur_count > max_count:
                    max_count = cur_count
            elif num ==0:
                cur_count = cur_count
            else:
                cur_count = 0
        if nums != []: 
            return(max_count+1)
        else:
            return(0)