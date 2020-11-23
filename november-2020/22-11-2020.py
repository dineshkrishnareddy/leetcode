"""
Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        length = len(words)

        if length == 0:
            return 0

        transformations = []
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for word in words:
            transformation = []
            for char in word:
                transformation.append(morse_codes[ord(char) - ord('a')])

            transformations.append(''.join(transformation))
        # print(transformations)
        return len(set(transformations))
