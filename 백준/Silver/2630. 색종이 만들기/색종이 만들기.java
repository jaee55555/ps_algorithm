//0624 [6]
//백준 2630

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[][] spaces;
	static int blue = 0;
	static int white = 0;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		spaces = new int[n][n];
		
		//데이터 입력 
		for(int i = 0; i < n; i++) { //가로  
			for(int j = 0; j < n; j++) { //세로 
				spaces[i][j] = sc.nextInt();
			}
		}
		
		//재귀호출
		recursiveCut(0, 0, n); //시작 행(세로) index, 시작 열(가로) index, 한변의 길이 
		System.out.println(white);
		System.out.println(blue);
		
		
		sc.close();
	}//main
	
	private static void recursiveCut(int rowIdx, int colIdx, int length) {
		
		int sum = 0;
		for(int i = rowIdx; i < rowIdx + length; i++) { //행 index
			for(int j = colIdx; j < colIdx + length; j++) { //열 index 
				sum += spaces[i][j];
			}
		}
		
		if(sum == length*length) { //전체 파란색 색종이 
			blue++;
			
		}else if(sum == 0) { //전체 하얀색 색종이 
			white++;
			
		}else {
		
			int newLength = length/2;
			//4등분된 영역에 대해 재귀호출 ==> 서로 일치하지 않는 색을 만났을 때 
			recursiveCut(rowIdx,             colIdx,             newLength); //좌상 
			recursiveCut(rowIdx,             colIdx + newLength, newLength); //우상 
			recursiveCut(rowIdx + newLength, colIdx,             newLength); //좌하 
			recursiveCut(rowIdx + newLength, colIdx + newLength, newLength); //우하
		}
		
	}//recursiveCut

}//class end
