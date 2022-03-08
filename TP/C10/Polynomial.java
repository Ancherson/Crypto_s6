
public class Polynomial {
    private int degree;
    private int[] coeff;

    /**
     * 
     * @param generate an array with p and coeffs from X
     * @param s
     */
    public Polynomial(int[] generate, int s) {
        degree = generate.length - 1;
        coeff = new int[generate.length];
        coeff[0] = s;
        for (int i = 1; i < generate.length; i++) {
            coeff[i] = generate[i];
        }
    }

    public int eval(int value) {
        int result = 0;
        for (int i = 0; i < coeff.length; i++) {
            result += coeff[i] * Math.pow(value, i);
        }
        return result;
    }

}