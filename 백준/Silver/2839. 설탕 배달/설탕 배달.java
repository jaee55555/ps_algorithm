//0624 [4]
//백준 2839
//written by jaee55555

import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sugar = sc.nextInt();
		
		
		
		if(sugar % 5 == 0) {
			System.out.println(sugar/5);
		}else {
			int cnt = 0;
			while(sugar > 0) {
				sugar -= 3;
				cnt += 1;
				
				if(sugar % 5 == 0) {
					cnt += sugar / 5;
					System.out.println(cnt);
					break;
				}else if(sugar == 1 || sugar == 2) {
					System.out.println("-1");
					break;
				}else if(sugar == 0) {
					System.out.println(cnt);
					break;
				}
			}
		}
		
		sc.close();
	}//main

}//class end
