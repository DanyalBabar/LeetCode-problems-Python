#   LeetCode Problem #520
#
#   Given a word, you need to judge whether the usage of capitals in it is right or not.
#
#   We define the usage of capitals in a word to be right when one of the following cases holds:
#
#   All letters in this word are capitals, like "USA".
#   All letters in this word are not capitals, like "leetcode".
#   Only the first letter in this word is capital if it has more than one letter, like "Google".
#   Otherwise, we define that this word doesn't use capitals in a right way.
#
#   Runtime: 44ms, 99.56th percentile


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
