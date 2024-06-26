import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1629_곱셈 {

    static int A, B, C;
    static int answer;

    // A를 B번 곱한 수를 C로 나눔 (A*B가 아님!)
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        answer = pow(A, B, C);
        System.out.println(answer);
        
    }

    private static int pow(int a, int b, int m){
        if(b==1) return a % m;
        int val = pow(a, b/2, m);
        val = val * val % m;
        if(b%2 == 0) return val;
        return val * a % m;
    }

}
