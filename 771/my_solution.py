class Solution(object):
    def numJewelsInStones(self, J, S):    
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        matches = 0
        for char in S:
            if char in J:
                matches += 1
        return matches
