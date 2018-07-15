class Solution(object):
    def peakIndexInMountainArray(self, A):
        for i in xrange(len(A)):
            if A[i] > A[i+1]:
                return i

# Complexity Analysis
# Time Complexity: O(N), where N is the length of A.

# Space Complexity: O(1).
