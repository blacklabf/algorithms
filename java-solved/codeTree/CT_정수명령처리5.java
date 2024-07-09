import java.util.*;
import java.io.*;


public class CT_정수명령처리5 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        ArrayList<Integer> v = new ArrayList<>();
        int N = Integer.parseInt(br.readLine());
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if(command.equals("push_back")){
                int val = Integer.parseInt(st.nextToken());
                v.add(val);
            }else if(command.equals("pop_back")){
                v.remove(v.size()-1);
            }else if(command.equals("size")){
                System.out.println(v.size());
            }else{
                int val = Integer.parseInt(st.nextToken());
                System.out.println(v.get(val-1));
            }
        }

    }
}