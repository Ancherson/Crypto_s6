import java.math.BigInteger;
import java.util.Random;

public class Main {

    private static int n = 10;
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
    public static int[] generate(int m, int k) {
        int[] gen = new int[k + 1];

        BigInteger bi = BigInteger.valueOf(m + 1);
        while (!bi.isProbablePrime(100) && bi.compareTo(BigInteger.valueOf((int) Math.pow(2, n))) < 0) {
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

    /**
     * 
     * @param p      ???
     * @param k
     * @param agents
     * @return
     */
    public static int coalition(int p, int k, Agent[] agents) {
        if (agents.length < k + 1) {
            System.out.println("Not enough agents.");
            System.exit(0);
        }

        int s = 0;
        for (int i = 1; i <= k+1; i++) {
            System.out.println(i);
            int numerator = 1;
            int denominator = 1;

            // Lagrange Formula
            for (int j = 1; j <= k+1; j++) {
                if (j != i) {
                    numerator *= -j;
                    denominator *= i - j;
                }
            }
            s += agents[i-1].getKey() * numerator / denominator;
        }

        return s;
    }

    public static void main(String[] args) {
        int k = 7;
        int s = 200;

        int[] gen = generate(n, k);

        System.out.println(gen[0]);

        System.out.println("Generated Polynomial :");
        Polynomial p = new Polynomial(gen, s);
        System.out.println(p);

        distribute(n, k , gen, s);
        System.out.println("Value given to agents :");
        for (Agent agent : agents)
            System.out.println(agent);

        System.out.println("Coalition's result :" + String.valueOf(coalition(gen[0], k, agents)));

    }
}
