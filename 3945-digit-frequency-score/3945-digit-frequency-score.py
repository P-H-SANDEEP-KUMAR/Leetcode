class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq={}
        li=list(str(n))
        mi=0
        for i in li:
            freq[int(i)]=freq.get(int(i),0)+1
        for key,value in freq.items():
            mi+=key*value
        return mi
