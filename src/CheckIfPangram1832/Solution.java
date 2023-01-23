package CheckIfPangram1832;

import java.util.ArrayList;

public class Solution {
    public boolean checkIfPangram(String sentence){
        ArrayList<Character> allLetters = new ArrayList<>();
        for (int i = 0; i <=25; i++) {
            allLetters.add((char) (i+97));
        }
        for (Character c :
                sentence.toCharArray()) {
            allLetters.remove(c);
            if (allLetters.isEmpty()){
                return true;
            }
        }
       return false;
    }


}
