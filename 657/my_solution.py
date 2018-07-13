class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x_pos = 0
        y_pos = 0
        
        for char in moves:
            if char == 'U':
                y_pos += 1
            elif char == 'D':
                y_pos -= 1
            elif char == 'R':
                x_pos += 1
            elif char == 'L':
                x_pos -= 1
        
        return x_pos == 0 and y_pos == 0
