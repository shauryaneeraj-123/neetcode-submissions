class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the lengths differ, they can't be anagrams.
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        # Count letters in s.
        for letter in s:
            if letter not in countS:
                countS[letter] = 1
            else:
                countS[letter] += 1

        # Count letters in t.
        for letter in t:
            if letter not in countT:
                countT[letter] = 1
            else:
                countT[letter] += 1

        # Compare the two dictionaries.
        return countS == countT