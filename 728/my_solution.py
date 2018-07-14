class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for i in range(left, right+1):
            num = str(i)
            self_dividing = True
            for char in num:
                if char == '0':
                    self_dividing = False
                    break
                if i % int(char) != 0:
                    self_dividing = False
                    break
            if self_dividing == True:
                output.append(i)
        return output
