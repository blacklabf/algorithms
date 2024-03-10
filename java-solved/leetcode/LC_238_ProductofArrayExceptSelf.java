package Implementation;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC_238_ProductofArrayExceptSelf {
    public static int[] productExceptSelf(int[] nums) {

        int[] ans = new int[nums.length];
        List<Integer> zeroIdx = new ArrayList<>();

        int tmp = 1;

        for(int i=0; i<nums.length; i++){
            if(nums[i]==0){
                zeroIdx.add(i);
            }else{
                tmp *= nums[i];
            }
        }

        for(int i=0; i<nums.length; i++){
            if(!zeroIdx.contains(i) && zeroIdx.size()!=0){
                // 무조건 0이있다는 소리
                ans[i] =0;
            }else if(zeroIdx.contains(i) && zeroIdx.size()>1){
                ans[i] = 0;
            }else if(zeroIdx.contains(i) && zeroIdx.size()==1){
                ans[i] = tmp;
            }
            else if(nums[i]!=0){
                ans[i] = tmp/nums[i];
               
            }
        }

        return ans;

    }

    public static void main(String[] args) {
        int[] input = {-1,1,0,-3,3};
        int[]  ans = productExceptSelf(input);
    System.out.println(Arrays.toString(ans));
    }
  
}
