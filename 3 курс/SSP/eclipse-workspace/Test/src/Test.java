import java.util.Random;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;
public class Test {
	/*
 		1.	Реализовать программу для создания  массива переменных String
		и инициализировать массив с названиями месяцев от января до декабря.
 		Создать массив, содержащий 12 случайных десятичных значений между 0.0 и 100.0.
 		Вывести название каждого месяца вместе с соответствующим десятичным значением.
 		Вычислить и вывести среднее значение 12 значений.
	 */
	public static void FirstTask(){
		String[] Months = new String[] {"Январь","Февраль","Март","Апрель",
										"Май","Июнь","Июль","Август",
										"Сентябрь","Октябрь","Ноябрь","Декабрь"};
		double[] Randomfloats = new double[12];
		Random random = new Random();
		System.out.println(String.format("%-10s | %-10s","Months","Floats"));
		for( int i = 0; i < Months.length && i < Randomfloats.length; i++ ) {
			Randomfloats[i] = random.nextDouble()*100.0;
			System.out.println(String.format("%-10s | %f",Months[i],Randomfloats[i]));
			
		}
		
	}
	/*
		2.	Реализовать программу для создания  массива из десяти переменных String, 
		каждая из которых содержит произвольную строку - месяц/день/год, например 01/09/2022. 
		Проанализировать каждый элемент в массиве и вывести представление 
		даты в формате 01 сентября 2022
	 */
	public static void SecondTask(){
		String[] Months = new String[] {"Январь","Февраль","Март","Апрель",
				"Май","Июнь","Июль","Август",
				"Сентябрь","Октябрь","Ноябрь","Декабрь"};
		String[] dates = new String[10];
        Random random = new Random();
        // Заполняем массив случайными датами в формате "месяц/день/год"
        for (int i = 0; i < dates.length; i++) {
            int month = random.nextInt(12) + 1;
            int day = random.nextInt(28) + 1;
            int year = random.nextInt(10) + 2020;
            dates[i] = String.format("%02d/%02d/%04d", month, day, year);
        }

        // Разделяем каждую дату на отдельные строки
        for (String date : dates) {
            String[] parts = date.split("/");
            int month = Integer.parseInt(parts[0]);
            

            // Выводим дату в формате "день месяц год"
            System.out.println(parts[1] + " " + Months[month-1] + " " + parts[2]);
        }
	}
	/*
		3.	Написать программу для создания случайной последовательности N прописных букв,
 		которая не включает гласные буквы.
	 */
	public static void ThirdTask() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Введите размер строки: ");
		int countN = sc.nextInt();
		Random random = new Random();
		String vowels = new String("eyuioa");
		char ascii = ' ';
		for(int i=0;i<countN;) {
			ascii = (char)(random.nextInt(123-97)+97);
			if(vowels.indexOf(ascii) == -1) {
				System.out.print(ascii);
				i++;
			}
		}
		sc.close();
		System.out.println();
	}
	/*
		4.	Создать объект типа String и проинициализировать его текстовой строкой.
 		Определить количество гласных, пробелов и общее количество букв.
	 */
	public static void FourthTask() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Введите строку: ");		
		String str = sc.nextLine();
		str = str.toLowerCase();
		String vowels = new String("eyuioa");
		int vowelsCount = 0,spacesCount = 0,charsCount = 0;
		for(int i=0;i<str.length();i++) {
			if(str.charAt(i) == ' ') {spacesCount++; continue;}
			if(vowels.indexOf(str.charAt(i)) != -1) {vowelsCount++;charsCount++;continue;}
			if(str.charAt(i)>=97 && str.charAt(i)<=122) {charsCount++;continue;}
		}
		System.out.println("Кол-во гласных: "+vowelsCount+"\nКол-во пробелов: "+spacesCount+"\nКол-во букв: "+charsCount);
	}
	/*
		5.	Создать массив объектов типа String и проинициализировать его текстовой строкой.
	 	Извлечь из массива строки по введенному разделителю. 
	 */
	public static void FifthTask() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Введите строку: ");		
		String str = sc.nextLine();
		System.out.print("Введите разделитель: ");	
		String separator = sc.nextLine();
		String[] parts = str.split(separator);
		for(String part : parts) {
			System.out.println(part);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 try {
	            System.setOut(new java.io.PrintStream(System.out, true, "UTF-8"));
	     } catch (UnsupportedEncodingException e) {
	            System.err.println("UTF-8 encoding not supported!");
	     }

	 	//FirstTask();
		//SecondTask();
		//ThirdTask();
		//FourthTask();
		//FifthTask();
	}

}
