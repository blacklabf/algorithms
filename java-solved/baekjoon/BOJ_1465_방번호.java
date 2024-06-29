import java.io.*;
import java.util.Arrays;

public class BOJ_1465_방번호 {
    
    // 한 세트 0~9 숫자가 하나씩
    // 다솜 방번호 주어짐 -> 필요한 세트의 개수
    // 6 = 9
    // 방번호 N <= 1,000,000 이 주어질 떄, 필요한 갯수 출력


    // N이 쉼표까지 주어졌을 떄, 고려
    // charAt(), toCharArray(), 문자열 길이, String.valueOf()
    static String N;
    static int[] nums;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = br.readLine();
        // 0부터 9까지 10개의 배열을 만들고 idx 별로 숫자 있을 때 추가, 6이나 9는 모두 6에 추가
        nums = new int[10];
        for(int i=0; i<N.length(); i++){
            int tmp = Integer.parseInt(String.valueOf(N.charAt(i)));
            if(tmp == 6 || tmp == 9){
                nums[6]++;
            }else{
                nums[tmp]++;
            }
        }

        // 최댓값을 찾고 만약 그게 6에 해당하는 거라면 두번쨰 최댓값과 나누기 2한 값을 찾아봄 
        // -> 저렇게 하지 말고 6의 값을 일단 2로 나눈 다음에 최댓값 비교 

        if(nums[6] % 2 == 0) {
            nums[6] = nums[6] / 2;
        }else{
            nums[6] = (nums[6]+1) /2 ;
        }

        int ans = Arrays.stream(nums).max().orElseThrow();
        System.out.println(ans);

        

        


        
    }
}
