package Implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SwitchTest {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[] switchs = new int[n];
		int[] tmp = new int[m];

		st = new StringTokenizer(br.readLine()); // st를 객체생성해서 new 해서 덮어 씌움
		for (int i = 0; i < m; i++) {
			tmp[i] = Integer.parseInt(st.nextToken());
			
		}

		
		for (int i = 0; i < m; i++) {
			for (int j = tmp[i]-1; j < n; j += tmp[i]) {
//				System.out.println(j);
				if (switchs[j] == 0) {
					switchs[j] = 1;
				} else  {
					switchs[j] = 0;
				}
			}
//			System.out.println(Arrays.toString(switchs));
		}
		for (int num : switchs) {
			System.out.print(num + " ");
		}
	}
}

