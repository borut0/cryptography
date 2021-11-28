import java.util.*;
public class polyalphabetic{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter plain text:");
		String plntxt = scan.nextLine();

		char txt[] = plntxt.toCharArray();

		System.out.print("Enter the key:");
		String key = scan.nextLine();

		String nkey=key;

		HashMap<Integer,Character> map = new HashMap<>();
		char ch='a';
		for(int i=0;i<26;i++){
			map.put(i,ch);
			ch++;
		}

		int intans[] = new int[100];
		int temp1=0,temp2=0;
		char ans[] = new char[plntxt.length()];

		System.out.println("Enter your Choice");
		System.out.println("1. with Key\n2. witout Key");
		int choice = scan.nextInt();

		switch(choice){
			case 1:
				while(nkey.length() < plntxt.length()){
					nkey += key;
				}
				if(nkey.length() > plntxt.length()){
					nkey = nkey.substring(0,nkey.length()-(nkey.length()-plntxt.length()));
				}

				char akey[] = nkey.toCharArray();

				 for(int i=0;i<plntxt.length();i++){
					for(Map.Entry m:map.entrySet()){
						if((Character)m.getValue() == txt[i]){
							temp1 = (Integer)m.getKey();
						}
						if((Character)m.getValue() == akey[i]){
							temp2 = (Integer)m.getKey();
						} 
						
						intans[i] = (temp1 + temp2)%26;

						for(Map.Entry e:map.entrySet()){
							if(intans[i] == (Integer)e.getKey()){
								ans[i] = (Character)e.getValue();
							}
						}
					}
				}

				System.out.print("Ans is ");
				for(int i=0;i<ans.length;i++){
					System.out.print(ans[i]);
				}
				break;

			case 2:
				nkey = key + plntxt;
				if(nkey.length() > plntxt.length()){
					nkey = nkey.substring(0,nkey.length()-(nkey.length()-plntxt.length()));
				}
				
				char wokey[] = nkey.toCharArray();

				 for(int i=0;i<plntxt.length();i++){
					for(Map.Entry m:map.entrySet()){
						if((Character)m.getValue() == txt[i]){
							temp1 = (Integer)m.getKey();
						}
						if((Character)m.getValue() == wokey[i]){
							temp2 = (Integer)m.getKey();
						} 
						
						intans[i] = (temp1 + temp2)%26;

						for(Map.Entry e:map.entrySet()){
							if(intans[i] == (Integer)e.getKey()){
								ans[i] = (Character)e.getValue();
							}
						}
					}
				}
				System.out.print("Ans is ");
				for(int i=0;i<ans.length;i++){
					System.out.print(ans[i]);
				}
				break;

			default:
				System.out.println("Wrong choice");
		}
	}
}
