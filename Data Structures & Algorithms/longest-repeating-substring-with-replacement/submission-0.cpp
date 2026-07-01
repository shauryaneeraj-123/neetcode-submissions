class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);

        int left = 0;
        int best = 0;
        int maxFreq = 0;

        for (int right = 0; right < s.size(); right++) {
            count[s[right] - 'A']++;

            maxFreq = max(maxFreq, count[s[right] - 'A']);

            int windowSize = right - left + 1;

            while (windowSize - maxFreq > k) {
                count[s[left] - 'A']--;
                left++;
                windowSize = right - left + 1;
            }

            best = max(best, right - left + 1);
        }

        return best;
    }
};