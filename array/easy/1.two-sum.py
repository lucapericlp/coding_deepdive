#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.17%)
# Total Accepted:    1.8M
# Total Submissions: 4.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		num_map = {}
		for index,num in enumerate(nums):
			num_map[num] = index
		
		for index,num in enumerate(nums):
			complement = target - num
			if complement in num_map and num_map[complement] != index:
				return [index,num_map[complement]]
		
		return []
			
			         
