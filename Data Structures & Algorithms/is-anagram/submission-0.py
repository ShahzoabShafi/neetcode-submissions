from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_t = defaultdict(int)
        hashmap_s = defaultdict(int)
        for letter in s:
            hashmap_s[letter] += 1
        for letter in t:
            hashmap_t[letter] += 1
        if hashmap_t == hashmap_s:
            return True
        else:
            return False
            