package DataStructure;

public class LC_121_BestTimetoBuyandSellStock {
    public static int maxProfit(int[] prices) {
        
        int start = prices[0];
        int n = prices.length;
        int ans = 0;

        for(int i=0; i<n-1; i++){
            if(start<prices[i]) continue;
            else{
                start = prices[i];
                for(int j=i+1; j<n; j++){
                    if(prices[i]<prices[j]) {
                        ans = Math.max(prices[j]-prices[i], ans);
                    }
                    else continue;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(maxProfit(prices));
    }
}