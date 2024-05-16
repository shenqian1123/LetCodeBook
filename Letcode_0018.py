from typing import List

"""
技巧：对于要求返回数组元素而非数组下标的题目，可以先排序后求解；
对于偏数学题目，适当剪枝可以提升效率
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        len_nums = len(nums)
        result = list()
        for i in range(len_nums):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            if ((len_nums - i) >= 4 and nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target):
                continue
            if ((len_nums - i) >= 4 and nums[i] + nums[-1] + nums[-2] + nums[-3] < target):
                continue
            for elem in self.threeSum(target-nums[i], nums[i+1:]):
                result.append([nums[i]] + elem)
            # result.append([elem + [nums[i]] for elem in self.threeSum(target-nums[i], nums[i+1:])])
        return result

    def threeSum(self, target, nums):
        len_nums = len(nums)
        result = list()
        for i in range(0, len_nums):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            if ((len_nums - i) >= 3 and nums[i] + nums[i+1] + nums[i+2] > target):
                continue
            if ((len_nums - i) >= 3 and nums[i] + nums[-1] + nums[-2] < target):
                continue
            for elem in self.twoSum(target-nums[i], nums[i+1:]):
                result.append([nums[i]] + elem)
            # result.append([elem + [nums[i]] for elem in self.twoSum(target-nums[i], nums[i+1:])])
        return result
    
    def twoSum(self, target, nums):
        len_nums = len(nums)
        result = list()
        i = 0
        j = len_nums - 1
        while i < j:

            # if ((len_nums - i) >= 2 and nums[i] + nums[i+1] > target):
            #     i = i + 1
            #     continue
            # if ((len_nums - i) >= 2 and nums[i] + nums[-1] < target):
            #     i = i + 1
            #     continue
            if i > 0 and nums[i] == nums[i - 1]:
                i = i + 1
                continue
            if j < len_nums - 1 and nums[j] == nums[j + 1]:
                j = j - 1
                continue
            if nums[i] + nums[j] == target:
                result.append([nums[i], nums[j]])
                i = i + 1
                j = j - 1


            if nums[i] + nums[j] > target:
                j = j - 1
            if nums[i] + nums[j] < target:
                i = i + 1


        return result 







if __name__ == "__main__":
    sl = Solution()
    result = sl.fourSum(nums=[-3,-2,-1,0,0,1,2,3], target=0)
    print(result)