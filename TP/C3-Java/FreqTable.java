import java.util.ArrayList;
import java.util.HashMap;

/**
 * Class that represents the four frequency tables in order to crack the key
 * Each table is represent by a HashMap and are stocked in an ArrayList.
 * 
 * @author Nico
 */
public class FreqTable {
    private ArrayList<HashMap<Character, Integer>> freq;

    /**
     * Constructor
     */
    public FreqTable() {
        freq = new ArrayList<HashMap<Character, Integer>>(4);
        for (int i = 0; i < 4; i++) {
            freq.add(new HashMap<Character, Integer>());
        }
    }

    /**
     * Increments the number associated with a character
     * Adds the key and the value 1 if the key doesn't exist.
     * 
     * @param tableIndex     the index in freq
     * @param tableCharIndex the key character
     */
    public void add(int tableIndex, Character tableCharIndex) {
        if (freq.get(tableIndex).containsKey(tableCharIndex)) {
            freq.get(tableIndex).put(tableCharIndex, freq.get(tableIndex).get(tableCharIndex) + 1);
        } else {
            freq.get(tableIndex).put(tableCharIndex, Integer.valueOf(1));
        }
    }

    /**
     * Getter
     * 
     * @return the frequency tables
     */
    public ArrayList<HashMap<Character, Integer>> getFreq() {
        return freq;
    }

    /**
     * Get the most frequent character in each table
     * 
     * @return an arraylist with the most frequent character in each table
     */
    public ArrayList<Character> getMaxFreq() {
        ArrayList<Character> list = new ArrayList<>(4);
        for (HashMap<Character, Integer> hm : freq) {
            Character max = 0;
            Integer m = 0;

            for (Character c : hm.keySet()) {
                if (hm.get(c).intValue() > m.intValue()) {
                    max = c;
                    m = hm.get(c);
                }
            }
            list.add(max);
        }
        return list;
    }

}
