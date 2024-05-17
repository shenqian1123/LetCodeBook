
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        len_nums = len(nums)
        period_list = list()

        left = 0
        right = 0
        while True:
            if right > len_nums - 1:
                period_list.append(right - left)
                break
            if nums[right] == 0:
                period_list.append(right - left)
                right = right + 1
                left = right
            else:
                right = right + 1


        return max(period_list)