class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            row.reverse()
        inverse = []
        for row in A:
            new_row = []
            for char in row:
                if char == 0:
                    new_row.append(1)
                elif char == 1:
                    new_row.append(0)
            inverse.append(new_row)
        return inverse
