//백준 2798
//written by jaee55555

import java.util.Arrays;
import java.util.Scanner;

public class Main{
	static int N; static int M;
	static int max = 0; static int temp = 0;
	static int[] nums; //숫자들 담을 저장소 
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); M = sc.nextInt(); //변수 입력 받기
		nums = new int[N]; 
		
		for(int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		Arrays.sort(nums); // 정렬해주기 
//		System.out.println(Arrays.toString(nums));
		
		for(int i = 0; i < N; i++) {
			int temp1 = nums[i];
			for(int j = i+1; j < N; j++) {
				int temp2 = temp1 + nums[j];
				if(temp2 < M) {
					for(int t = j+1; t < N; t++) {
						int temp3 = temp2 + nums[t];
						if(temp3 == M) {
							max = temp3;
							
							break;
						}
						else if(temp3 < M && temp3 >= max) {
							max = temp3;
						}
						else if(temp3 > M) {
							break;
						}
					}
				}//t
			}//j
			
		}//i
		
		if(max <= M) System.out.println(max);
		sc.close();
		
	}//main
	

}//class end
