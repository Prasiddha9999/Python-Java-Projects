import java.util.*;
public class Strtraverse
{
    public static Hashtable numVowelsConsonants(String let){
        Hashtable vowCon = new Hashtable();
        int vowelCount = 0;
        int consCount = 0;
        for (int i = 0;  i < let.length(); i++){
         if (let.charAt(i) == 'a' || let.charAt(i) == 'e' || let.charAt(i) == 'i' || let.charAt(i) == 'o' || let.charAt(i) == 'u'){
            vowelCount++;
        }else if (let.charAt(i) >= 'a' && let.charAt(i) <= 'z'){
            consCount++;
            }
        }
        vowCon.put("Vowels",vowelCount);
        vowCon.put("Consonants", consCount);
        return vowCon;
    }
    public static void main(String[] args){
        Scanner tex = new Scanner(System.in);
        System.out.println("Enter a String: ");
        String usInp = tex.nextLine();
        Hashtable out = numVowelsConsonants(usInp);
        System.out.println("Number of vowels and consonants are: " +out);
    }
}
