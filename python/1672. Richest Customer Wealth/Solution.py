class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        biggest = 0
        for account in accounts:
            temp = sum(account)
            if biggest < temp:
                biggest = temp
        return biggest
