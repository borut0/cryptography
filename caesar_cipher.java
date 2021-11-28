import java.util.*;
public class caesar_cipher{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		HashMap<Integer,Character> map = new HashMap<>();
		char ch='a';
		for(int i=0;i<26;i++){
			map.put(i,ch);
			ch++;
		}

		System.out.print("Enter plain Text:");
		String txt = scan.nextLine();

		System.out.println();

		System.out.print("Enter key:");
		int key = scan.nextInt();

		int intans[] = new int[100];
		char ans[] = new char[txt.length()];

		char pntxt[] = txt.toCharArray();

		for(int i=0;i<txt.length();i++){
			for(Map.Entry m:map.entrySet()){
				if((Character)m.getValue() == pntxt[i]){
					intans[i] = ((Integer)m.getKey()+key)%26;
					for(Map.Entry e:map.entrySet()){
						if(intans[i] == (Integer)e.getKey()){
							ans[i] = (Character)e.getValue();
						}
					}
				}
			}
		}

		System.out.print("Ans is ");
		for(int i=0;i<ans.length;i++){
			System.out.print(ans[i]);
		}
	}
}
