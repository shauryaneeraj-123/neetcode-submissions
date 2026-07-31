from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(f"{len(s)}#{s}")

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        parts = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            parts.append(s[start:end])

            i = end

        return parts