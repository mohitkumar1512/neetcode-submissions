class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # We can use the naive approach to simulate the queue one purchase at a time which would take time proportional to the total number of tickets. Instead we can use a single pass counting algorithm

        target = tickets[k]
        if target == 0: return 0

        total_time = 0

        for i, count in enumerate(tickets):
            if i <= k:

                total_time += min(count, target)
            
            else:
                total_time += min(count, target - 1)
            
        return total_time