class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_substring = set()
        left=0
        max_length = 0

        for right in range(len(s)):
            while s[right] in window_substring:
                window_substring.remove(s[left])
                left+=1
            window_substring.add(s[right])
            max_length = max(max_length,right - left + 1)
        
        return max_length

                # window_substring = ""
        # for char in s:
        #     if char not in window_substring:
        #         window_substring += char
        #     else:
        #         break

        # longest_substring = len(window_substring)
        # left = 0

        # for right in range(len(window_substring), len(s)):
        #     while s[right] in window_substring:
        #         window_substring = window_substring[left + 1 :]

        #     window_substring += s[right]
        #     longest_substring = max(longest_substring, len(window_substring))

        # return longest_substring

