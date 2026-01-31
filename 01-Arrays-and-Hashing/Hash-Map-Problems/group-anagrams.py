"""
LeetCode 49: Group Anagrams
Difficulty: Medium
Topic: Arrays & Hashing - Hash Map Problems

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
* 1 <= strs.length <= 1000
* 0 <= strs[i].length <= 100
* strs[i] is made up of lowercase English letters
"""

from typing import List


class Solution:
    """
    Solution 1: Sorting Approach
    Time Complexity: O(m * n log n) where m = number of strings, n = max string length
    Space Complexity: O(m)
    
    Intuition:
    - Anagrams have the same characters, so when sorted they become identical
    - Use sorted string as the key to group anagrams together
    """
    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            # Sort the string to create a unique key for anagrams
            sorted_str = ''.join(sorted(s))
            
            # Group strings with the same sorted key
            res[sorted_str] = res.get(sorted_str, []) + [s]
        
        return list(res.values())
    
    
    """
    Solution 2: Character Count Array (Optimal)
    Time Complexity: O(m * n) where m = number of strings, n = max string length
    Space Complexity: O(m)
    
    Intuition:
    - Count frequency of each character (a-z) in an array of size 26
    - Anagrams will have identical frequency arrays
    - Use tuple of frequency array as the dictionary key
    - Faster than sorting because counting is O(n) vs sorting O(n log n)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            # Create frequency count array for a-z (26 letters)
            count = [0] * 26
            
            # Count frequency of each character
            for c in s:
                # ord(c) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
                count[ord(c) - ord('a')] += 1
            
            # Convert list to tuple (lists can't be dict keys)
            key = tuple(count)
            
            # Group strings with the same character frequency
            res[key] = res.get(key, []) + [s]
        
        return list(res.values())


# Alternative implementations without using .get()

class SolutionAlt:
    """Solution 1 Alternative: Using if-check instead of .get()"""
    def groupAnagrams_sorting_v2(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            # Check if key exists first
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(s)
        
        return list(res.values())
    
    
    """Solution 2 Alternative: Using if-check instead of .get()"""
    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            
            # Check if key exists first
            if key not in res:
                res[key] = []
            res[key].append(s)
        
        return list(res.values())
    
    
    """Solution 2 Alternative: Using .setdefault()"""
    def groupAnagrams_v3(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            res.setdefault(key, []).append(s)
        
        return list(res.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 60)
    print("Testing Solution 1: Sorting Approach")
    print("=" * 60)
    
    # Test 1
    test1 = ["act","pots","tops","cat","stop","hat"]
    result1 = solution.groupAnagrams_sorting(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print()
    
    # Test 2
    test2 = ["x"]
    result2 = solution.groupAnagrams_sorting(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print()
    
    # Test 3
    test3 = [""]
    result3 = solution.groupAnagrams_sorting(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print()
    
    print("=" * 60)
    print("Testing Solution 2: Character Count Array (Optimal)")
    print("=" * 60)
    
    # Test 1
    result1 = solution.groupAnagrams(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print()
    
    # Test 2
    result2 = solution.groupAnagrams(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print()
    
    # Test 3
    result3 = solution.groupAnagrams(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print()
    
    print("=" * 60)
    print("Comparison:")
    print("Solution 1 (Sorting): O(m * n log n) - Easy to understand")
    print("Solution 2 (Counting): O(m * n) - Optimal performance")
    print("=" * 60)