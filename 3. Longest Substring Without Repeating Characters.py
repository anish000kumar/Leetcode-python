''' 
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        currCount = 0
        maxCount = 0
        left = right = 0

        while (right < len(s)):
            if(s[right] not in hashmap):
                hashmap[s[right]] = True
                currCount += 1
                maxCount = max(maxCount, currCount)
                right += 1
            else:
                while s[right] in hashmap:
                    del hashmap[s[left]]
                    left += 1
                    currCount -= 1

        return maxCount
