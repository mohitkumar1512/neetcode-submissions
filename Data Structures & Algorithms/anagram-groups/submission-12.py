class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for char in s:
                # ord() gives the ASCII value; subtracting ord('a') maps 'a'->0, 'b'->1, etc.
                count[ord(char) - ord('a')] += 1
            
            # Convert the list to a tuple so it can be used as a dictionary key
            counter[tuple(count)].append(s)
        
        return list(counter.values())
