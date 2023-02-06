# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution(object):
    def runningSum(self, nums):
        result = []
        accum = 0
        for n in nums:
            accum += n
            result.append(accum)
        return result
