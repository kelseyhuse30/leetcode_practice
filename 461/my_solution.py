class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        x_len = len(x_bin)
        y_len = len(y_bin)
        len_diff = x_len - y_len
        
        if len_diff > 0:
            y_bin = y_bin.zfill(x_len)
        elif len_diff < 0:
            x_bin = x_bin.zfill(y_len)
        
        diff = 0
        
        for i, digit in enumerate(x_bin):
            if digit != y_bin[i]:
                diff += 1
        return diff
