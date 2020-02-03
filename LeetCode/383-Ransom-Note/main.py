class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magazineMap = {}
        
        for letter in magazine:
            if letter in magazineMap:
                magazineMap[letter] += 1
            else:
                magazineMap[letter] = 1
                
        for letter in ransomNote:
            if letter in magazineMap and magazineMap[letter] > 0:
                magazineMap[letter] -= 1
            else:
                return False
            
        return True
