class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cheapest = prices [0];
        int bestProfit = 0;

        for (int i = 1; i< prices.size(); i++){
            int profitToday = prices[i]-cheapest;

            bestProfit = max(bestProfit, profitToday);
            cheapest = min(cheapest, prices[i]);
        }
        return bestProfit;
    }
};
