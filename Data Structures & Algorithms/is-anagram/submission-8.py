class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the strings have different lengths,
        # they CANNOT contain the same number of letters.
        if len(s) != len(t):
            return False

        # Dictionary that will count each character.
        count = {}

        # Go through every character in s.
        for char in s:

            # If char is already in the dictionary,
            # add 1 to its count.
            if char in count:
                count[char] += 1

            # Otherwise, this is the first time
            # we have seen this character.
            else:
                count[char] = 1


        # Now go through every character in t.
        for char in t:

            # If t contains a character that was
            # not even in s, they cannot be anagrams.
            if char not in count:
                return False

            # Remove one occurrence because
            # we found the same character in t.
            count[char] -= 1

            # If the count goes below 0,
            # t has MORE of this character than s.
            if count[char] < 0:
                return False


        # If we reached here, every character matched.
        return True