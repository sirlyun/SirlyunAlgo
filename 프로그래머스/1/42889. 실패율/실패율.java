class Solution {
    public int[] solution(int N, int[] people) {
        // stage 생성
        int[] stages = new int[N+1];
        int[] check = new int[N];
        double[] fail = new double[N];
        int[] result = new int[N];

        for (int i=0; i<people.length; i++){
            stages[people[i]-1] += 1;
        }

        for (int i=0; i<N; i++){
            result[i] = i+1;
            for (int j=i+1; j<N+1; j++){
                check[i] += stages[j];
            }
        }

        for (int i=0; i<N; i++){
            fail[i] = (double) stages[i] / check[i];
        }

        double a = 0;
        int b = 0;
        for (int i=0; i<N; i++){
            for (int j=1; j<N-i; j++){
                if (fail[j-1]<fail[j]){
                    a = fail[j-1];
                    fail[j-1] = fail[j];
                    fail[j] = a;

                    b = result[j-1];
                    result[j-1] = result[j];
                    result[j] = b;
                }
            }
        }

        return result;
    }
}