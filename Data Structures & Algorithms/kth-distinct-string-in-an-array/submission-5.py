class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        distinct = [s for s in c if c[s] == 1]
        return distinct[k - 1] if k <= len(distinct) else ""