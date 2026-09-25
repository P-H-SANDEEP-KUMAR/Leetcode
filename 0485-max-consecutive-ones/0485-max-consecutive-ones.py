class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        maxm_cnt=0
        for i in nums:
            if i==1:
                cnt+=1
                maxm_cnt=max(maxm_cnt,cnt)
            else:
                cnt=0
        return maxm_cnt