# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/

class Solution:
    def combinationSum(self, candidates, target):
    	"""
    	return a list of all unique combinations of candidates where the choosen numbers sum to target.
    	
		@ Knapsack problem to find best fit
    	"""
    	dp = [[] for _ in range(target + 1)]

    	dp[0] = [[]]

    	for num in candidates:
    		for i in range(num, len(dp)):
    			dp[i].extend(comb + [num] for comb in dp[i - num])
    	return dp[-1]




if __name__ == '__main__':
	a = Solution()
	print(a.combinationSum([2,3,5], 8))