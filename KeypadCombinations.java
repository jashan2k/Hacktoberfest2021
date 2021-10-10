import java.util.Scanner;

public class KeypadCombinations{
	
	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		System.out.print("Enter a number : ");
		String str = s.next();
		System.out.println();
		System.out.println("The Keypad Combinations are :-\n");
		printKeypad(str, "");
	}
	
	static String[] Keypads = {".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"};
	
        private static void printKeypad(String input, String output){
        if(input.length() == 0) {
            	System.out.println(output);
            	return;
        }
	char ch = input.charAt(0);
        String remInput = input.substring(1);
	String Elements = Keypads[ch - '0'];
        for(int i = 0 ; i < Elements.length() ; i++){
		char chr = Elements.charAt(i);
		printKeypad(remInput, output + chr);
        }
    }
}
