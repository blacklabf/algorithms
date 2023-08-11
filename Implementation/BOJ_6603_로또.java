package Implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_6603_로또 {
    static int K, S[], numbers[];
    static boolean flag;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        // 0이 들어올 때까지 입력받는 거 해야 함.
        while (flag==false) {
            st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());
            if(K==0){
                flag = true;
                return;
            }
            S = new int[K];
            numbers = new int[6];
            for (int i = 0; i < K; i++) {
                S[i] = Integer.parseInt(st.nextToken());
            }
            comb(0, 0);
            System.out.println();
        }

    }

    private static void comb(int cnt, int start) {

        if (cnt == 6) {
            for(int idx=0; idx<6; idx++){
                System.out.print(numbers[idx]);
                System.out.print(" ");
            }
            System.out.println();
            return;
        }
        for (int i = start; i < K; i++) {
            numbers[cnt] = S[i];
            comb(cnt + 1, i + 1); // start+1 이면 계속 바뀐다고 했잖아!! -> 정확하게 알고 있기! 
        }
    }
}
