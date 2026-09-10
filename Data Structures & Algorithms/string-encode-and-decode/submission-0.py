from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += (f"{len(string)}#{string}")

        return output

    def decode(self, s: str) -> List[str]:

        output = list()
        idx = 0
        temp_str = ""
        
        while idx < len(s):
            j = idx
            while s[j] != '#':
                j+=1
            length = int(s[idx:j])
            temp_str = s[j+1:j+1 + length]
            output.append(temp_str)
            idx = j+1 + length
        
        return output


            
