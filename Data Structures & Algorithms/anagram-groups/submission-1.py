class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        twoSum = {}

        for string in strs:
            setString = ''.join(sorted(string))
            if twoSum:
                if setString in twoSum:
                    twoSum[setString].append(string)
                else:
                    twoSum[setString] = [string]
            else:
                twoSum[setString] = [string]

        return list(twoSum.values())