from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        i = 0
        j = i + 1
        while True:
            if i > len_nums - 1:
                break
            if j > len_nums - 1:
                break
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                if i == j:
                    pass
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                j = j + 1

        return i+1
    

if __name__ == "__main__":
    sl = Solution()
    result = sl.removeDuplicates(nums=[1,1,2])
    print(result)