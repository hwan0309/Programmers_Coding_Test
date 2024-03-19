package Coding_Test_Easy;

import java.util.Scanner;

public class Coding_Test_01 {

	public static void main(String[] args) {
		
	Scanner sc = new Scanner(System.in);
	
	int a, b;
	a = sc.nextInt();
	b = sc.nextInt();
	
	if(a > 0 && b < 10) {
		System.out.println(a+b);
	}else {
		System.out.println();
	}
	}

}
