
import java.util.*;
import java.io.*;

public class BOJ_3273_두수의합{

    static int N, ans, cnt;
    static int[] nList;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(br.readLine());
        nList = new int[N];
        for(int i=0; i<N; i++){
            nList[i] = Integer.parseInt(st.nextToken());
        }

        ans = Integer.parseInt(br.readLine());
        cnt = 0;

        for(int i=0; i<N-1; i++){
            for(int j=i+1; j<N; j++){
                if(nList[i]+nList[j]==ans){
                    cnt ++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}

