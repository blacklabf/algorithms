
import java.util.Arrays;

public class LC_1_TwoSum {

    public static int[] twoSum(int[] nums, int target) {

        int[] ans = new int[2];

        for(int i=0; i<nums.length-1; i++){
            for(int j=i+1; j<nums.length; j++){
                if(nums[i]+nums[j]==target){
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return ans;   
    }

    // test
    public static void main(String[] args) {
        int[] input = {2,7,11,15};
        int target = 9;
        int[] ans = twoSum(input, target);
        System.out.println(Arrays.toString(ans));
    }
}
