class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer than s2, it is impossible for s2
        # to contain a permutation of s1.
        if len(s1) > len(s2):
            return False

        # Stores the frequency of each character in s1.
        # This is the target we want our window in s2 to match.
        s1_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        # Stores the frequency of characters in the current window of s2.
        window_count = {}

        # Left pointer marks the start of our sliding window.
        left = 0

        # The window size should always equal len(s1).
        for right in range(len(s2)):

            # Add the current character into our window.
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # If the window becomes larger than s1,
            # remove the leftmost character to keep the same size.
            if right - left + 1 > len(s1):

                window_count[s2[left]] -= 1

                # Remove characters with frequency 0
                # to keep the dictionary clean.
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # If the current window has the same character frequencies
            # as s1, then the window is a permutation of s1.
            if window_count == s1_count:
                return True

        # No valid permutation was found.
        return False