import CheckIfPangram1832.CheckIfPangram;
public class Main {
    public static void main(String[] args) {
        CheckIfPangram checkIfPangram = new CheckIfPangram();
        boolean result = checkIfPangram.checkIfPangram("thequickbrownfoxjumpsoverthelazydog");
        System.out.println(result);

    }
}