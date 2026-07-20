class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        high=0
        for customer in accounts:
            wealth=sum(customer)
            high=max(high,wealth)
        return high
        