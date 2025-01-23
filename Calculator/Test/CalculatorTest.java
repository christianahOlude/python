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
}
    @Test
    public void testThatTenPositiveNumbersCanBeAdded() {
        Calculator calc3 = new Calculator();
        int number = 1;
        int numberTwo = 2;
        int numberThree = 3;
        int numberFour = 4;
        int numberFive = 5;
        int numberSix = 6;
        int numberSeven = 7;
        int numberEight = 8;
        int numberNine = 9;
        int numberTen = 10;
        int expectedResult = calc3.addition(number, numberTwo, numberThree, numberFour, numberFive, numberSix, numberSeven, numberEight, numberNine, numberTen);
        assertEquals(55, expectedResult);
    }
    @Test
    public void testThatFivePositiveNumbersCanBeSubtracted() {
        Calculator calc4 =  new Calculator();
        int firstNumber = 1;
        int secondNumber = 2;
        int thirdNumber = 3;
        int fourthNumber = 4;
        int fifthNumber = 5;
        int expectedResult = calc4.subtraction(firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber);
        assertEquals(-15, expectedResult);
    }
    @Test
    public void testThatAcceptsFloat(){
        Calculator calc = new Calculator();
        float number = 1.1f;
        float numberTwo = 2.2f;
        float expectedResult = calc.decimal(number,  numberTwo);
        assertEquals(3.0f, expectedResult);
}




}