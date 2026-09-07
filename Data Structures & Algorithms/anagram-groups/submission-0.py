from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        output_array = []
        
        for word in strs:

            sorted_key = "".join(sorted(word))
            hashmap[sorted_key].append(word)
        
        return list(hashmap.values())