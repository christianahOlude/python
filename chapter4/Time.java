public class Time{

public static void main(String... args){
//int firstNumber = 10;
//int secondNumber =50;
//int sum = firstNumber + secondNumber;
//System.out.println(sum);

add(50, 100);
divide(122,22);
subtract(90, 50);
multiplication(12,6);

}



public static void add(int firstNumber, int secondNumber)
{
	int sum = firstNumber + secondNumber;
	System.out.println(sum);

}

public static void divide(int firstNumber, int secondNumber){

	int division = firstNumber / secondNumber;
	System.out.println(division);

}

public static void subtract(int firstNumber, int secondNumber){

	int subtract = firstNumber - secondNumber;
	System.out.println(subtract);

}
public static void multiplication(int firstNumber, int secondNumber){

	int multiplication = firstNumber * secondNumber;
	System.out.println(multiplication);
}

}