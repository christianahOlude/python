public class Calculator {

    public int addition(int... num) {
        int sum = 0;
        for (int add : num) {
            sum += add;
        }
        return sum;
    }
    public int subtraction(int... num) {
        int sub = 0;
        for (int minus : num) {
            sub -= minus;

        }
        return sub;
    }
    public int decimal(float... num) {
         int sum = 0;
        for (float add : num) {
            sum += add;
        }
            return sum;
    }

}
