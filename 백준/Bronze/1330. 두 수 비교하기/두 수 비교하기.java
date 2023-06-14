import java.io.*;

public class Main{
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		String[] array = br.readLine().split(" ");
		int A = Integer.parseInt(array[0]);
		int B = Integer.parseInt(array[1]);
		String res = "";
		if(A>B) {
			res = ">";
		} else if(A<B) {
			res = "<";
		} else {
			res = "==";
		}
		System.out.print(res);
	}
}