class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dick = {}
        if len(s) != len(t):
            return False

        for ch in s:
            dick[ch] = dick.get(ch, 0) + 1
        
        for ch in t:
            if ch not in dick:
                return False
            dick[ch] -= 1
            if dick[ch] < 0:
                return False

        return True