import java.util.*;
import java.io.*;

public class CT_수열조작 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> dq = new ArrayDeque<>();
        for(int i=1; i<=N; i++){
            dq.add(i);
        }

        while(dq.size()>=2){
            dq.remove();
            int tmp = dq.remove();
            dq.add(tmp);
        }

        System.out.println(dq.poll());
    }
}