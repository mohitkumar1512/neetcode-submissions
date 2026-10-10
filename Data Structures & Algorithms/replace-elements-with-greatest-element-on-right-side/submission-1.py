class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # we can iterate in reverse and keep track of the greatest

        greatest = -1 
        for i in range(len(arr) -1, -1, -1):
            greatest, arr[i] = max(greatest, arr[i]), greatest
        
        return arr