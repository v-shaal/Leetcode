''' ''''''
 [383] Ransom Note

 https://leetcode.com/problems/ransom-note/description/


 
 Given an arbitrary ransom note string and another string containing letters
 from all the magazines, write a function that will return true if the ransom 
 note can be constructed from the magazines ; otherwise, it will return
 false. 
 
 
 Each letter in the magazine string can only be used once in your ransom
 note.
 
 
 Note:
 You may assume that both strings contain only lowercase letters.
 
 
 
 canConstruct("a", "b") -> false
 canConstruct("aa", "ab") -> false
 canConstruct("aa", "aab") -> true
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return all(ransomNote.count(x) <= magazine.count(x) for x in set(ransomNote))
