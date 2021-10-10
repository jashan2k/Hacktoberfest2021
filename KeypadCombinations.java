import java.util.Scanner;

public class KeypadCombinations {
	
	public static void main(String[] args){
		
		Scanner s = new Scanner(System.in);
		System.out.print("Enter a number : ");
		int input = s.nextInt();
		System.out.println();
		System.out.println("The Keypad Combinations are :\n");
		printKeypad(input);
	}

	public static void printKeypad(int input){
        printKeypad(input,"");
	}
	
    private static void printKeypad(int input,String output){
        if(input == 0) {
            System.out.println(output);
            return;
        }
        String smallAns[]=helper(input%10); 
        for(int i = 0;i < smallAns.length; i++){
            printKeypad(input/10,smallAns[i]+output);
        }
    }
    
    private static String[] helper(int n){
        if(n == 0) {
            String ans[]={".",";"};
            return ans;
        }
        else if(n == 1){
            String ans[]={"a","b","c"};
            return ans;
        }
        else if(n == 2){
            String ans[]={"d","e","f"};
            return ans;            
        }
        else if(n == 3){
            String ans[]={"g","h","i"};
            return ans;            
        }
        else if(n == 4){
            String ans[]={"j","k","l"};
            return ans;            
        }
        else if(n == 5){
            String ans[]={"m","n","o"};
            return ans;            
        }
        else if(n == 6){
            String ans[]={"p","q","r","s"};
            return ans;            
        }
        else if(n == 7){
            String ans[]={"t","u"};
            return ans;            
        }
        else if(n == 8){
            String ans[]={"v","w","x"};
            return ans;            
        }
        else if(n == 9){
            String ans[]={"y","z"};
            return ans; 
        }
        String ans2[]={" "};
        return ans2;
	}
}
