from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for word in strs:

            sorted_key = "".join(sorted(word))

            if sorted_key not in hashmap:
                hashmap[sorted_key] = []

            hashmap[sorted_key].append(word)
        
        return list(hashmap.values())