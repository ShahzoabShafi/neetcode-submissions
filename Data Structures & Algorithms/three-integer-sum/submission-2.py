class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = list()
        target = 0
        for idx, num in enumerate(nums):
            first_digit_for_sum = num
            if idx > 0 and first_digit_for_sum == nums[idx - 1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                remaining_target = target - first_digit_for_sum
                current_sum = nums[l] + nums[r]
                if current_sum < remaining_target:
                    l += 1
                elif current_sum > remaining_target:
                    r -= 1
                else:
                    if [first_digit_for_sum, nums[l], nums[r]] not in output:
                        output.append([first_digit_for_sum, nums[l], nums[r]])
                    l += 1
                    r -= 1
        return output
