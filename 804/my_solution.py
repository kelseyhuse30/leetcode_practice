class Solution(object):
    def mor(self, char):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        if char == 'a':
            return morse[0]
        elif char == 'b':
            return morse[1]
        elif char == 'c':
            return morse[2]
        elif char == 'd':
            return morse[3]
        elif char == 'e':
            return morse[4]
        elif char == 'f':
            return morse[5]
        elif char == 'g':
            return morse[6]
        elif char == 'h':
            return morse[7]
        elif char == 'i':
            return morse[8]
        elif char == 'j':
            return morse[9]
        elif char == 'k':
            return morse[10]
        elif char == 'l':
            return morse[11]
        elif char == 'm':
            return morse[12]
        elif char == 'n':
            return morse[13]
        elif char == 'o':
            return morse[14]
        elif char == 'p':
            return morse[15]
        elif char == 'q':
            return morse[16]
        elif char == 'r':
            return morse[17]
        elif char == 's':
            return morse[18]
        elif char == 't':
            return morse[19]
        elif char == 'u':
            return morse[20]
        elif char == 'v':
            return morse[21]
        elif char == 'w':
            return morse[22]
        elif char == 'x':
            return morse[23]
        elif char == 'y':
            return morse[24]
        elif char == 'z':
            return morse[25]
        else:
            return ''
    
    def uniqueMorseRepresentations(self, words):
        morse_words = []
        for word in words:
            morse_word = ''
            for char in word:
                morse_word += self.mor(char)
            if morse_word not in morse_words:
                morse_words.append(morse_word)
        return len(morse_words)
        """
        :type words: List[str]
        :rtype: int
        """
