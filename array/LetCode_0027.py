from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        i = 0
        j = len_nums
        while True:
            j = j - 1
            if (j <= -1):
                break
            if nums[j] == val:
                continue
            else:
                break

        while True:
            if (i < j):
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
                    while True:
                        if (j <= -1):
                            break
                        if (nums[j] == val):
                            j = j - 1
                        else:
                            break
                else:
                    i = i + 1
            elif (i == j):
                while True:
                    if (j <= -1):
                        break
                    if (nums[j] == val):
                        j = j - 1
                    else:
                        i = j 
                        break
                break
            else:
                i = j
                break
        return i + 1
    
if __name__ == "__main__":
    sl = Solution()
    nums = [4,2,0,2,2,1,4,4,1,4,3,2]
    result = sl.removeElement(nums=nums, val=4)
    print(result)
    print(nums)