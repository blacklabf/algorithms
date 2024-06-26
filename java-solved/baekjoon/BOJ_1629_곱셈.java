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

        int start = A % C;

        for(int i=1; i<B; i++){
            start = reminder(start * A, C);
        }
        System.out.println(start);
        
    }

    private static int reminder(int dividend, int divisor){
        answer = dividend % divisor;
        return answer;
    }

}
