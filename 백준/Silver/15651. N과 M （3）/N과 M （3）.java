//0620
//백준 15651
//written by jaee55555

import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static int[] arr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); // 1~N까지의 정수  
		M = sc.nextInt(); // M개 조합 뽑기 
		
		arr = new int[M];
		
		findNums(0);
		sc.close();
		System.out.println(sb);
		
	}//main
	
	static void findNums(int depth) {
		if (depth == M) { //깊이가 뽑아야하는 숫자의 갯수와 같을 때 
			for(int i = 0; i < M; i++) {
//				System.out.print(arr[i] + " ");
				sb.append(arr[i]).append(' ');
			}
//			System.out.println();
			sb.append('\n');
			return;
		}
		
		for(int i = 0; i < N; i++) {
			arr[depth] = i+1; 
			findNums(depth+1);
		}
	}//findNums
	


}//class end
