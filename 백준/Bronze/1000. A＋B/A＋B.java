import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException{
		String[] array = br.readLine().split(" ");
		
//		int B = Integer.parseInt(br.readLine());
		int C = Integer.parseInt(array[0]) + Integer.parseInt(array[1]);
		System.out.println(C);

	}

}
