import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    @Test
    public void testThatTwoPositiveNumbersCnBeAdded() {
        Calculator calc = new Calculator();
        int firstNumber = 1;
        int secondNumber = 2;
        int expectedResult = calc.addition(firstNumber, secondNumber);
        assertEquals(3, expectedResult);

    }
   @Test
        public void testThatTwoNegativeNumbersCanBeAdded() {
            Calculator calc2 = new Calculator();
            int firstNumber = -1;
            int secondNumber = -2;
            int expectedResult = calc2.addition(firstNumber, secondNumber);
            assertEquals(-3, expectedResult);
}public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}