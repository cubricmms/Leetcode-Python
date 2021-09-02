# Leetcode problem 3 (Longest Substring Without Repeating Characters):
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Level: Medium


# Sliding window approach
# learned from https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3:-sliding-window-O(N)-with-explanation

"""
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output, index, seen = 0, 0, {}
        for cursor, char in enumerate(s):
            if char not in seen:
                # walk through the non-repeated substring
                output = max(output, cursor - index + 1)
            else:
                if seen[char] < index:
                    # [Review: tricky part]
                    # since char is outside the current window
                    # the previous output should already record the longest non-repeated string with char inside
                    # it is safe to move forward, the char can be treat as fresh.
                    output = max(output, cursor - index + 1)
                else:
                    # if the char is seen and within the current window
                    # move index to the right of the seen char
                    index = seen[char] + 1

            seen[char] = cursor
        return output


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert solution.lengthOfLongestSubstring(s="bbbbb") == 1
    assert solution.lengthOfLongestSubstring(s="pwwkew") == 3
    assert solution.lengthOfLongestSubstring(s="") == 0
    assert solution.lengthOfLongestSubstring(s="a") == 1
    assert solution.lengthOfLongestSubstring(s="au") == 2
    assert solution.lengthOfLongestSubstring(s="auc") == 3
    assert solution.lengthOfLongestSubstring(s="aab") == 2
    assert solution.lengthOfLongestSubstring(s="abcaerwef") == 6
