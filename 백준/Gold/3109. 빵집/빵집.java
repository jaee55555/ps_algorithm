//0625
//백준 3109
//written by jaee55555

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int R;
	static int C;
	static char[][] matrix;
	static int answer = 0;
	public static void main(String[] args) throws Exception {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		matrix = new char[R][C];
		
		for(int i = 0; i < R; i++) {
			String str = br.readLine();
			for(int j = 0; j < C; j++) {
				matrix[i][j] = str.charAt(j);
			}
//			System.out.println(Arrays.toString(matrix[i]));
		}//배열 받기
		
//		for(int i=0; i<R; i++)
//			matrix[i] = br.readLine().toCharArray();
		
		
		for(int i = 0; i < R; i++) {
			if(checkPipe(i, 0)) {
				answer += 1;
			}
		}
		
		System.out.println(answer);
		
	}//main
	
	public static boolean checkPipe(int x, int y) {
		matrix[x][y] = '-';
		
		
		if(y == C-1) { //원웅이집 빵집에 도착하면 true 리턴
			return true;
		}
		
		//아직 빵집에 도착 안했을 때 
		//1. 오른쪽 위 
		if(x > 0 && matrix[x-1][y+1] == '.') {
			if(checkPipe(x-1, y+1)) return true;
		}
		//2. 오른쪽으로 쭉
		if(matrix[x][y+1] == '.') {
			if(checkPipe(x, y+1)) return true;
		}
		//3. 오른쪽 아래 
		if(x < R -1 && matrix[x+1][y+1] == '.') {
			if(checkPipe(x+1, y+1)) return true;
		}
		
		return false;
	
	}//checkPipe

}//class
