import java.io.*;
import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100;


        for (int i=0; i<n-1; i++){
            int[][] chk = new int[n-1][2];
            for (int j=0; j<n-1; j++){
                if (i == j){
                    continue;
                }
                chk[j] = wires[j];
            }
            int cnt = bfs(chk, n);
            answer = Math.min(answer, cnt);
        }



        return answer;
    }
    
    static int bfs(int[][] chk, int n){

        List<List<Integer>> graph = new ArrayList<>();

        for (int i=0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<n-1; i++){
            graph.get(chk[i][0]).add(chk[i][1]);
            graph.get(chk[i][1]).add(chk[i][0]);
        }

        int[] check = new int[n+1];
        int cnt = 1;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        check[1] = 1;
        while (!queue.isEmpty()){
            int now = queue.poll();

            for (int next : graph.get(now)){
                if (check[next] != 1){
                    check[next] = 1;
                    cnt += 1;
                    queue.add(next);
                }
            }
        }


        return Math.abs(n-2*cnt);
    }
}