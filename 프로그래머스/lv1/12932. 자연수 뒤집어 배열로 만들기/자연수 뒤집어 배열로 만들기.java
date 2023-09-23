class Solution {
    public int[] solution(long n) {
        char[] new_n = Long.toString(n).toCharArray();
        int[] answer = new int[new_n.length];
        for (int i=new_n.length-1; i>=0; i--){
            answer[new_n.length - 1 - i] = new_n[i] - '0';
        }
        return answer;
    }
}