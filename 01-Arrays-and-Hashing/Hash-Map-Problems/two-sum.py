"""
LeetCode 1: Two Sum
Difficulty: Easy
Topic: Arrays & Hashing - Hash Map Problems

Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
* 2 <= nums.length <= 1000
* -10,000,000 <= nums[i] <= 10,000,000
* -10,000,000 <= target <= 10,000,000
* Only one valid answer exists.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution - O(n²)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSumOptimal(self, nums: List[int], target: int) -> List[int]:
        # Hash Map Solution - O(n)
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    print(solution.twoSum([3,4,5,6], 7))  # Expected: [0,1]
    
    # Test 2
    print(solution.twoSum([4,5,6], 10))   # Expected: [0,2]
    
    # Test 3
    print(solution.twoSum([5,5], 10))     # Expected: [0,1]
    
    # Test optimal solution
    print("\nOptimal Solution:")
    print(solution.twoSumOptimal([3,4,5,6], 7))  # Expected: [0,1]