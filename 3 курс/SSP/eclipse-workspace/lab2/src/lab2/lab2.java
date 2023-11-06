package lab2;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class lab2 {
	static int typeOfSort = 0;
    public static void main(String[] args) {
        // Read input file path from command line argument
        String inputFilePath = "input.txt";
        
        // Read numbers from input file
        List<Integer> numbers = readNumbersFromFile(inputFilePath);
        if(IsSorted(numbers)) {
        	System.out.println("Is Sorted");
        }
        else {
        	System.out.println("Is Not Sorted");
        }
        // Sort numbers in ascending order
        Collections.sort(numbers);
        
        // Write sorted numbers to output file
        String outputFilePath = "output.txt";
        writeNumbersToFile(outputFilePath, numbers);
        
        System.out.println("Numbers sorted and written to output file successfully!");
    }
    private static boolean IsSorted(List<Integer> numbers) {
    	if(typeOfSort==0) {
    		for(int i=0;i<numbers.size()-1;i++) {
        		if(numbers.get(i)>numbers.get(i+1)) return false;
        	}	
    	}
    	else {
	    	for(int i=0;i<numbers.size()-1;i++) {
	    		if(numbers.get(i)<numbers.get(i+1)) return false;
	    	}
    	}
    	return true;
    }
    
    private static List<Integer> readNumbersFromFile(String filePath) {
        List<Integer> numbers = new ArrayList<>();
        
        try (Scanner scanner = new Scanner(new File(filePath))) {
        	
        	typeOfSort = scanner.nextInt();
            scanner.nextLine(); // Move to the next line
        	
        	int arrayLength = scanner.nextInt();
            scanner.nextLine(); // Move to the next line
            
            for (int i = 0; i < arrayLength; i++) {
                int number = scanner.nextInt();
                numbers.add(number);
            }
        } catch (IOException e) {
            System.out.println("Error reading input file: " + e.getMessage());
        }
        
        return numbers;
    }
    
    private static void writeNumbersToFile(String filePath, List<Integer> numbers) {
        try (FileWriter writer = new FileWriter(filePath)) {
        	if(typeOfSort==0) {
            for (int number : numbers) {
                writer.write(number + "\n");
            }}
        	else {
        	for (int i = numbers.size()-1;i>=0;i--) {
                    writer.write(numbers.get(i) + "\n");
            }}
        } catch (IOException e) {
            System.out.println("Error writing to output file: " + e.getMessage());
        }
    }
}
