
public class LC_121_BestTimetoBuyandSellStock {

    public static int maxProfit(int[] prices) {

        int n = prices.length;
        int ans = 0;
        int left = 0;
        int right = 1;

        while(right<n){
            if(prices[left]<prices[right]){
            ans = Math.max(ans,prices[right] -prices[left]);
            right++;
            }
            else{
                left = right;
                right++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(maxProfit(prices));
    }
}