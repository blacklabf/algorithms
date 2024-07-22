import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/*
 * 카드 : 1(젤위)~N(젤아래)
 * 1장 남을 때까지 반복
 *  - 제일 위의 카드를 버리고 그 다음 카드를 젤 마지막으로 옮긴다.
 * 마지막에 남는 카드느?  
 */

public class BOJ_2164_카드2 {

    static int N;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        Queue<Integer> queue = new ArrayDeque<>();
        
        for(int i=1; i<=N; i++){
            queue.add(i);
        }

        while (queue.size() >= 2) {
            queue.remove();
            int tmp = queue.remove(); 
            queue.add(tmp);
        }
        System.out.println(queue.poll());
    }
}
