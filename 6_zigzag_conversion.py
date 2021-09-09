# Leetcode problem 6 (ZigZag Conversion): https://leetcode.com/problems/zigzag-conversion/
# Level: Medium


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows <= 1:
            return s

        result = ""
        # use length of the repeated pattern as stepper
        # |P|(0, 0)   |A|   |H|   |N|
        # |A|(0, 1) P |L| S |I| I |G|
        # |Y|(0, 2)   |I|   |R|
        # above marked chars all have a distance of lenOfCharPattern to its left one
        lenOfCharPattern = numRows + (numRows - 2)
        for i in range(numRows):
            for j in range(i, len(s), lenOfCharPattern):
                result += s[j]

                # since zigzag pattern might produce at most one more char to the right
                if i == 0 or i == numRows - 1:
                    continue

                distance_to_paired = ((numRows - 1) - i) * 2
                paired_index = j + distance_to_paired
                if paired_index < len(s):
                    result += s[paired_index]

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.convert(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
    assert solution.convert(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
