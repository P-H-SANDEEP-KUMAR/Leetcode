class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=len(nums)
        nums.sort()
        for i in range(m+1):
            if i not in nums:
                return i