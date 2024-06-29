import java.io.*;
import java.util.Arrays;

public class BOJ_1465_방번호 {
    
    static String N;
    static int[] nums;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = br.readLine();
        // nums[9]가 필요 없어서 0부터 8까지 크기 9의 배열 선언
        nums = new int[9]; 

        for (int i = 0; i < N.length(); i++) {
            int tmp = Character.getNumericValue(N.charAt(i));
            if(tmp==9) {nums[6]++;}
            else{nums[tmp]++;}
        }

        // 6과 9는 같이 사용 가능하므로 처리 : 홀수일 떄, 짝수일 때 상관없이 +1 후, 몫으로 계산
        nums[6] = (nums[6] + 1) / 2; // 최소 6과 9의 세트 개수

        // 6과 9를 제외한 다른 숫자들의 최대 세트 개수 계산
        // StreamAPI 사용
        int ans = Arrays.stream(nums).max().orElseThrow();
        System.out.println(ans);
    }
}
