
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2579_계단오르기 {

	// 계단 오르기를 할 때, dp[i]는 i번째 계단을 밟았을 경우만 생각을 함
	// i 계단을 안 밟는 경우는 i+1번째 계단에서 고려함
	// : 이게 아닌 이유 -> 마지막 계단의 경우 답을 출력할 때, dp[N], dp[N-1] 중 최댓값을 생각해서 마지막 계단을 밟았는지 안
	// 밟았는지에 대해 고민하면 됨
	// 첫계단이 아니라 마지막 계단을 무조건 밟아야 하네!!! => 문제를 잘 못 이해했는데 dp 배열자체는 제대로 이해함 : 그 전 틀린 코드로
	// 백준 확인
	static int[] dp;
	static int ans;
	static int N;
	static int[] stairs;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		stairs = new int[N + 1];
		for (int i = 1; i < N + 1; i++) {
			stairs[i] = Integer.parseInt(br.readLine());
		}
//		System.out.println(Arrays.toString(stairs));

		dp = new int[N + 1];
		if (N == 1) {
			System.out.println(stairs[1]);
//			dp[1] = stairs[1];
		} else if (N == 2) {
//			dp[1] = stairs[1];
			System.out.println(stairs[1] + stairs[2]);
		} else if (N == 3) {
			System.out.println(Math.max(stairs[1] + stairs[2], Math.max(stairs[1] + stairs[3], stairs[2] + stairs[3])));
		} else if (N > 3) { // N을 3 이상으로 하면 1을 선택하지 않았을 경우가 되네
			dp[1] = stairs[1];
			dp[2] = stairs[1] + stairs[2];
			for (int i = 3; i < N + 1; i++) {
				dp[i] = Math.max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i]);
			}
//			System.out.println(Arrays.toString(dp));

			System.out.println(dp[N]); // 최댓값이 아니라 무조건 맨 뒤에 있는 걸 밟았다고 해서 N 번째 index를 출력해야 함.
		}

	}

}