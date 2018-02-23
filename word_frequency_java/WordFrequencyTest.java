import java.util.Scanner;

public class WordFrequencyTest{

    private static void pt(String msg){
        System.out.println(msg);
    }

    public static void main(String [] args){
        // testing isValidWord Function
        pt("-----Testing isValidWord Function------");
        String goodWord1 = "Omar";
        String badWord1 = "$mar";
        System.out.printf("String %s is %s \n",goodWord1, WordFrequency.isValidWord(goodWord1));
        System.out.printf("String %s is %s \n", badWord1, WordFrequency.isValidWord(badWord1));
        pt("------");

        //Testing buildWordFrequencyTable
        pt("----Testing the buildWordFrequencyTable using custom String---");
        String testMsg = "My name is Omar and this has 8 words";
        WordFrequency wfTable = new WordFrequency();
        wfTable.buildWordFrequencyTable(testMsg);
        wfTable.printTable();
        pt("---------");

        pt("---Testing the wordFrequency Class using a File from Standard Input---");
        //Testing using a real input file
        String fileContent = "";
        Scanner reader = new Scanner(System.in);
        
        while(reader.hasNextLine()){
            fileContent += reader.nextLine() + "\n";
        }

        WordFrequency wfTable2 = new WordFrequency();
        wfTable2.buildWordFrequencyTable(fileContent);
        wfTable2.printTable();
    }
}
