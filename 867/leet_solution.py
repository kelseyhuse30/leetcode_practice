class Solution(object):
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans

        #Alternative Solution:
        #return zip(*A)
        
 
# Complexity Analysis

# Time Complexity: O(R * C), where R and C are the number of rows and columns in the given matrix A.

# Space Complexity: O(R * C), the space used by the answer. 
