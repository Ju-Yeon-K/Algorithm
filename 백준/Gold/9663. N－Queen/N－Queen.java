import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static int N;
    public static int cnt = 0;

    public static boolean promising(int[] arr, int idx){
        for(int i=0; i<idx;i++){
            if (arr[i] == arr[idx] || Math.abs(arr[i] - arr[idx]) == idx - i) {
                return false;
            }
        }
        return true;
    }

    public static void nqueen(int[] arr, int idx){
        if (idx == N){
            cnt += 1;
        }
        else {
            for(int i=1; i<N+1; i++){
                arr[idx] = i;
                if (promising(arr, idx)){
                    nqueen(arr, idx + 1);
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        int[] chess = new int[N];

        nqueen(chess, 0);
        System.out.print(cnt);

    }
}
