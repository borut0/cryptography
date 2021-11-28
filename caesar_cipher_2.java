import java.util.Scanner;
public class caesar_cipher_2{
	public static void main(String args[]){
		System.out.print("Enter plain Text:");
		Scanner scan = new Scanner(System.in);
		String str = scan.nextLine();

		System.out.print("Enter k :");
		int k = scan.nextInt();

		char ch[] = str.toCharArray();

		System.out.print("Ans is :");
		for(int i=0;i<str.length();i++){
			for(int j=0;j<k;j++){
				ch[i]++;
			}
			System.out.print(ch[i]);
		}
	}
}
