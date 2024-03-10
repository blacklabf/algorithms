import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;

class PG_기능개발{
    public static LinkedList<Integer> solution(int[] progresses, int[] speeds) {

        LinkedList<Integer> answer = new LinkedList<>();
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        int N = progresses.length;

        for (int i = 0; i < N; i++) {
            q1.add(progresses[i]);
            q2.add(speeds[i]);
        }

        int day = 1;
        int cnt = 1;

        while (!q1.isEmpty()) {
            int a1 = q1.poll();
            int a2 = q2.poll();
            if (a1 + a2 * day < 100) {
                answer.add(cnt);
                if ((100 - a1) % a2 != 0) {
                    day = (100 - a1) / a2 + 1;
                } else {
                    day = (100 - a1) / a2;
                }
                cnt = 1;
            } else {
                cnt++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] progresses = {93,30,55};
        int[] speeds = {1,30,5};
        System.out.println(solution(progresses, speeds));
    }
}