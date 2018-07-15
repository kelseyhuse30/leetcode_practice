class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        isMountain = 1
        peak = None
        
        for i in range(len(A)-1):
            if A[i] < A[i+1] > A[i+2]:
                peak = i+1
                for j in range(peak, len(A)-1):
                    if A[j] < A[j+1]:
                        isMountain = 0
                        break
                break

            elif A[i] < A[i+1] < A[i+2]: 
                isMountain = 1
            else:
                isMountain = 0
                break
        
        if isMountain:
            return peak
        else:
            return None
