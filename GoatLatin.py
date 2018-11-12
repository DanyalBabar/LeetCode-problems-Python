#   LeetCode Problem #824
#
#   A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
#
#   We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#
#   The rules of Goat Latin are as follows:
#
#   If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#   For example, the word 'apple' becomes 'applema'.
#
#   If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#   For example, the word "goat" becomes "oatgma".
#
#   Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#   For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
#   Return the final sentence representing the conversion from S to Goat Latin.
#
#
#   Runtime: 36ms, 98.22th percentile

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = ""
        words = S.split()
        VOWELS = "aeiouAEIOU"

        count = 1;

        for i in words:
            if i[0] in VOWELS:
                result = result + i + "ma" + count * "a" + " "
            else:
                i = i + i[0] + "ma" + count * "a"
                result += i[1:] + " "
            count += 1

        return result[0:len(result)-1]
