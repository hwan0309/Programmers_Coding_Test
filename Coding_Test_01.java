package Coding_Test_Easy;

import java.util.Scanner;

public class Coding_Test_01 {
	
	// A + B
	//두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
	
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
