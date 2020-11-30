import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Akif_Megaprime_extracredit {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] firstLast = scanner.nextLine().split(" ");
        long first = Long.parseLong(firstLast[0]);

        long last = Long.parseLong(firstLast[1]);
        
        // Write Your Code Here
        int cntr = 0;
        for (int i = (int)first; i <= (int)last; i++){
            if (isMegaPrime(i)){
                cntr++;
            }
        }
        System.out.println(cntr);

        scanner.close();
    }
    
    public static boolean checkDigits(int n) { 
        while (n > 0) { 
            int dig = n % 10; 
  
            // check if digits are prime or not 
            if (dig != 2 && dig != 3 &&  
                dig != 5 && dig != 7) 
                return false; 
  
            n /= 10; 
        } 
  
        return true; 
    } 
      
    public static boolean prime(int num) { 
        if (num == 1) 
            return false; 
  
        for (int i = 2; i <= num/2; i++) { 
            if (num % i == 0){
                return false;
            } 
        } 
  
        return true; 
    } 
      
    public static boolean isMegaPrime(int num) { 
        return (checkDigits(num) && prime(num)); 
    } 

}