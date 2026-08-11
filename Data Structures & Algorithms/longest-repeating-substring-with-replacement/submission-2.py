class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Stores how many times each character appears in the current window.
        count = {}

        # Left pointer marks the beginning of the sliding window.
        left = 0

        # Stores the highest frequency of any single character
        # currently seen in the window.
        max_freq = 0

        # Stores the length of the longest valid substring found so far.
        longest = 0

        # Expand the window one character at a time.
        for right in range(len(s)):

            # Add the current character to the window.
            count[s[right]] = count.get(s[right], 0) + 1

            # Update the highest frequency character in the window.
            max_freq = max(max_freq, count[s[right]])

            # If more than k replacements are needed,
            # shrink the window from the left until it becomes valid again.
            while (right - left + 1) - max_freq > k:

                # Remove the leftmost character from the window.
                count[s[left]] -= 1

                # Move the left pointer to shrink the window.
                left += 1

            # Update the longest valid window found so far.
            longest = max(longest, right - left + 1)

        # Return the length of the longest substring that can be made
        # into one repeating character using at most k replacements.
        return longest