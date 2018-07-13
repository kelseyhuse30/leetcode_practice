class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
        
# Time Complexity: O(N), where N is the length of moves. We iterate through the string.

# Space Complexity: O(1). In Java, our character array is O(N).
