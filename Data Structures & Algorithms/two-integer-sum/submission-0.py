class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_list = {}

        for idx,num in enumerate(nums):
            remaining_target = target - num
            if remaining_target in num_to_list:
                return [num_to_list[remaining_target],idx]
            else:
                num_to_list[num] = idx
        return []