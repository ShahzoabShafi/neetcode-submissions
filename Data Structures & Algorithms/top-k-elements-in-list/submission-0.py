from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for number in nums:
            hashmap[number]+=1
        
        arr = []
        for number, count in hashmap.items():
            arr.append([count,number])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

        
        
            