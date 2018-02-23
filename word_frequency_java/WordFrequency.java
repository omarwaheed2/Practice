import java.util.StringTokenizer;
import java.util.HashMap;

public class WordFrequency{

    HashMap<String, Integer> wordFrequency;

    public WordFrequency(){
        wordFrequency = new HashMap<String, Integer>();
    }

    public void buildWordFrequencyTable(String words){
        StringTokenizer st = new StringTokenizer(words);
        String next;
        while (st.hasMoreTokens()){
            next = st.nextToken();
            // If not a space and is a valid word add to
            // hashmap and increment value appropriately
            if (!next.equals(" ") && isValidWord(next)){
                if (wordFrequency.containsKey(next)){
                    wordFrequency.put(next, wordFrequency.get(next) + 1);
                }else{
                    wordFrequency.put(next, 1);
                }
            }
        }
    }

    public void printTable(){
        System.out.println("\t Word \t Frequency");
        int totalWords = 0;
        for ( String word : wordFrequency.keySet() ){
            System.out.printf("\t %s \t %s\n", word, wordFrequency.get(word));
            totalWords += wordFrequency.get(word);
        }
        System.out.println("Total Words in the table : " + totalWords);
    }


    public static boolean isValidWord(String word){
        for (char c: word.toCharArray()){
            if ( (c < 'a' || c > 'z') &&
                 (c < 'A' || c > 'Z') 
               ){
                return false;            
            }
        }
        return true;
    }
}
