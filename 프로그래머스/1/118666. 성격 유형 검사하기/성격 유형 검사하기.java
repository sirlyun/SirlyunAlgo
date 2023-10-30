class Solution {
   public String solution(String[] survey, int[] choices) {
		String[] og = {"RT", "CF", "JM", "AN"};
        String[] rv = {"TR", "FC", "MJ", "NA"};

        int[][] chk = {
                {0, 0}, {0, 0}, {0, 0}, {0, 0}
        };
        
        String answer = "";

        // 점수 주기
        for (int i=0; i<survey.length; i++){
            int left = 0;
            int right = 0;
            int now = 0;

            for (int j=0; j<4; j++){
                if (survey[i].equals(og[j])){
                    now = j;
                    if (choices[i] < 4){
                        left += (4 - choices[i]);
                    } else if (choices[i] > 4) {
                        right += (choices[i] - 4);
                    }
                    break;
                } else if (survey[i].equals(rv[j])) {
                    now = j;
                    if (choices[i] < 4){
                        right += (4 - choices[i]);
                    } else if (choices[i] > 4) {
                        left += (choices[i] - 4);
                    }
                    break;
                }
            }

            chk[now][0] += left;
            chk[now][1] += right;
        }

        for (int i=0; i<chk.length; i++){
            if (chk[i][0] == chk[i][1]){
                answer += og[i].charAt(0);
            } else if (chk[i][0] < chk[i][1]){
                answer += og[i].charAt(1);
            } else {
                answer += og[i].charAt(0);
            }
        }


        return answer;
    }
}