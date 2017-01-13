import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_streak = 0
        current_word = ""

        for letter in s:
            if letter not in current_word:
                current_word += letter
                # print(letter, ", ", current_word, len(current_word))
            else:
                current_word = current_word[current_word.rindex(letter) + 1:] + letter

            if len(current_word) > longest_streak:
                longest_streak = len(current_word)

        return longest_streak


class TestSolution(unittest.TestCase):
    solver = Solution()

    def test_example1(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example2(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example3(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("pwwkew"), 3)

    def test_review1(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("aab"), 2)

    def test_review2(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("dvdf"), 3)

    def test_review3(self):
        self.assertEqual(self.solver.lengthOfLongestSubstring("bpfbhmipx"), 7)


if __name__ == '__main__':
    # unittest.main()
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))
