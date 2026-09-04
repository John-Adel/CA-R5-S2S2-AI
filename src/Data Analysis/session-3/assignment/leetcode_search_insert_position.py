# link: https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        copy = nums[:]
        while True:
            if len(copy) // 2 == 0 and target > copy[0]:
                return (nums.index(copy[0]) + 1)
            elif len(copy) // 2 == 0 and target < copy[0]:
                return (nums.index(copy[0]))
            elif target == copy[len(copy) // 2]:
                return nums.index(copy[len(copy) // 2])
            elif target > copy[len(copy) // 2]:
                copy = copy[len(copy) // 2 :]
            elif target < copy[len(copy) // 2]:
                copy = copy[: len(copy) // 2]