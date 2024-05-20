from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        left_zero = -1
        i = 0
        while (i < len_nums):
            if (left_zero == -1) and nums[i] == 0:
                left_zero = i
                i = i + 1
            elif (left_zero != -1) and nums[i] == 0:
                i = i + 1
            elif (left_zero != -1) and (i > left_zero) and nums[i] != 0:
                nums[i], nums[left_zero] = nums[left_zero], nums[i]
                left_zero = left_zero + 1
                i = i + 1
            else:
                i = i + 1
    
if __name__ == "__main__":
    sl = Solution()
    nums = [0,1,0,3,12]
    result = sl.moveZeroes(nums=nums)
    print(nums)