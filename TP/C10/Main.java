import java.math.BigInteger;
import java.util.Random;

public class Main {

    private static Agent[] agents;

    /**
     * Generates p and coeffs
     * 
     * p needs s :thinking:
     * 
     * @param k
     * @param m
     * @return
     */
    public static int[] generate(int k, int m) {
        int[] gen = new int[k + 1];

        BigInteger bi = BigInteger.valueOf(m + 1);
        while (!bi.isProbablePrime(100)) {
            bi = bi.add(BigInteger.ONE);
        }

        gen[0] = bi.intValue();

        Random rd = new Random();
        for (int i = 1; i < k + 1; i++) {
            gen[i] = rd.nextInt(gen[0]);
        }

        return gen;
    }

    /**
     * 
     * @param m
     * @param k   ???
     * @param gen
     * @param s
     */
    public static void distribute(int m, int k, int[] gen, int s) {
        Polynomial p = new Polynomial(gen, s);
        agents = new Agent[m];
        for (int i = 0; i < m; i++) {
            agents[i] = new Agent(i + 1, p.eval(i + 1));
        }
    }

    public static void main(String[] args) {
        // Test generate
        /*
         * int[] gen = generate(3, 30);
         * for (int i = 0; i < gen.length; i++) {
         * System.out.println(gen[i]);
         * }
         */
    }
}
