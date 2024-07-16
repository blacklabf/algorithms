import java.util.*;
import java.io.*;

public class CT_정수명령처리8 {

    static int N;



    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        LinkedList<Integer> l = new LinkedList<>();

        N = Integer.parseInt(br.readLine());
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if(cmd.equals("push_front")){
                int val = Integer.parseInt(st.nextToken());
                l.addFirst(val);
            }else if(cmd.equals("push_back")){
                int val = Integer.parseInt(st.nextToken());
                l.addLast(val);
            }else if(cmd.equals("pop_front")){
                System.out.println(l.pollFirst());
            }else if(cmd.equals("pop_back")){
                System.out.println(l.pollLast());
            }else if(cmd.equals("size")){
                System.out.println(l.size());
            }else if(cmd.equals("empty")){
                if(l.isEmpty()){
                    System.out.println(1);
                }else{
                System.out.println(0);
                }
            }else if(cmd.equals("front")){
                System.out.println(l.peekFirst());
            }else if(cmd.equals("back")){
                System.out.println(l.peekLast());
            }

        }
        
    }
}
