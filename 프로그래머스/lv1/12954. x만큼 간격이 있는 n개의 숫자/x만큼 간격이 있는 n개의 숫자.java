class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;
        int cnt = 1;
        while (cnt < n){
            answer[cnt] = answer[cnt-1]+x;
            cnt++;
        }
        return answer;
    }
}