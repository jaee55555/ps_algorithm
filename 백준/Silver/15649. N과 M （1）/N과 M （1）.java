import java.util.Scanner;
 
public class Main {
    
	public static int[] arr;
	public static boolean[] visit;
    public static int N;
    public static int M;
 
	public static void main(String[] args) {
 
		Scanner sc = new Scanner(System.in);
 
		N = sc.nextInt();
		M = sc.nextInt();
 
		arr = new int[M];
		visit = new boolean[N];
		findNums(N, M, 0);
        sc.close();
	}//main
 
	public static void findNums(int N, int M, int depth) {
		if (depth == M) {
			for (int val : arr) {
				System.out.print(val + " ");
			}
			System.out.println();
			return;
		}
 
		for (int i = 0; i < N; i++) {
			if (!visit[i]) {
				visit[i] = true;
				arr[depth] = i + 1;
				findNums(N, M, depth + 1);
				visit[i] = false;
			}
		}
	}//findNums
 
}//class end