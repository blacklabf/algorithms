// BOJ 2798 : 블랙잭

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int sum = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;

		st = new StringTokenizer(br.readLine());
		int[] card = new int[n];
		for (int i = 0; i < n; i++) {
			card[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(card);

		for (int i = n - 1; i >= 2; i--) {
			for (int j = i - 1; j >= 1; j--) {
				for (int k = j - 1; k >= 0; k--) {
					sum = card[i] + card[j] + card[k];

					if (m >= sum) {
						max = Integer.max(max, sum);
					}

				}
			}
		}
		System.out.println(max);

	}

}
