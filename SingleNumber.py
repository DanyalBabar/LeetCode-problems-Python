#   LeetCode Problem #136
#
#   Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
#   Runtime: 44ms, 77.58th percentile

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currNums = {

        }

        for i in nums:
            if i not in currNums:
                currNums[i] = 1
            else:
                del currNums[i]

        for i in currNums:
            if currNums[i] == 1:
                return i
