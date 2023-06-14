import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static int N, S;
    public static int[] nums;
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = sc.nextInt();
        nums = new int[N];
        for(int i=0; i<N; i++) {
            nums[i] = sc.nextInt();
        }

        int st = 0;
        int end = 0;
        int tempSum = nums[0];
        int res = N;

        while(st < N){
            if(tempSum >= S){
                int tempCnt = end - st + 1;
                if (tempCnt < res){
                    res = tempCnt;
                }
                tempSum -= nums[st];
                st += 1;
            } else if (end < N-1){
                end += 1;
                tempSum += nums[end];
            } else {
                break;
            }
        }
        if (st == 0){
            res = 0;
        }

        System.out.print(res);
    }

}