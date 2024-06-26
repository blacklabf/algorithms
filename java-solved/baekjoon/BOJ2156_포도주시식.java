
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ2156_포도주시식 {

	static int N;
	static int[] grapes;
	static int[] dp;
	// dp 배열 : 현재 그 잔을 선택했을 때의 가장 많은 양을 먹은 경우를 넣어줌 (그래서 마지막이 최댓값인지는 모름)
	// dp 자체는 내가 무조건 선택한 경우야 -> 코드를 수정하면 출력할 때 N-1 이랑 N이랑 고려하는 게 의미가 있나?
	// 2잔 연속 안 마시는 경우 6 1000 1000 1 1 1000 1000

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		dp = new int[N + 1]; // index 번호랑 몇번째인지 바로 쓸거임
		grapes = new int[N + 1]; // 처음 초기화하면 자연스레 0이 들어가서 0번째 index 0으로 설정 안해도됨.

		for (int i = 1; i < N + 1; i++) {
			grapes[i] = Integer.parseInt(br.readLine());
		}

		if (N == 1) {
			System.out.println(grapes[1]);
		} else if (N == 2) {
			System.out.println(grapes[1] + grapes[2]);
		} else if (N == 3) {
			System.out.println(Math.max(grapes[1] + grapes[2], Math.max(grapes[2] + grapes[3], grapes[1] + grapes[3])));
		} else {
			dp[1] = grapes[1];
			dp[2] = grapes[1] + grapes[2];
			dp[3] = Math.max(grapes[1] + grapes[2], Math.max(grapes[2] + grapes[3], grapes[1] + grapes[3]));
			for (int i = 4; i < N + 1; i++) { // dp로는 2가지 이지만 출력할 때 최댓값을 한 번 더 확인해서 출력하니까 N==3일 때 생각하면
				dp[i] = Math.max(dp[i - 3] + grapes[i - 1] + grapes[i],
						Math.max(dp[i - 2] + grapes[i], dp[i - 4] + grapes[i] + grapes[i - 1]));
				// 다음코드에 어떤 영향을 끼치지?
			}
			System.out.println(Math.max(dp[N - 1], dp[N]));
//			System.out.println(dp[N]); // 코드를 수정하면서 N번째에 전꺼를 선택하지 않는 경우도 들어가고 선택하는 경우도 다 포함되기때문에 이렇게 출력해도 됨 => 안돼 내 전까지만 선택할 수도 있잖아. 
		}

	}
}