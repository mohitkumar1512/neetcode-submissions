class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs: 
            key = tuple(sorted(string)) 
            res[key].append(string)
        
        result = []
        for k, v in res.items():
            temp = []
            for val in v:
                temp.append(val)
            result.append(temp)
        
        return result