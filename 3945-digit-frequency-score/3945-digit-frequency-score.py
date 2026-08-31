class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq={}
        li=list(str(n))
        mi=[]
        for i in li:
            freq[int(i)]=freq.get(int(i),0)+1
        for key,value in freq.items():
            mi.append(key*value)
        return sum(mi)
