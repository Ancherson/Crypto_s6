public class Agent {
    private final int id;
    private final int key;

    /**
     * An agent has an id and a key
     * 
     * @param id
     * @param key
     */
    public Agent(int id, int key) {
        this.id = id;
        this.key = key;
    }

    // Getters
    public int getId() {
        return id;
    }

    // Setters
    public int getKey() {
        return key;
    }
}
