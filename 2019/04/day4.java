package day4;

import java.util.stream.IntStream;

public class day4 {
    public static void main(String[] args) {
        int start = 372037;
        int end = 905157;

        System.out.println(IntStream.range(start,end).filter(day4::part1).count()); // range() -> like for loop, filter -> same as 'x -> part1(x)'
        System.out.println(IntStream.range(start,end).filter(day4::part2).count());

    }// END main


    public static boolean part1(int input){
        char[] numbers = Integer.toString(input).toCharArray(); // into char array -> easier to compare

        boolean isIncreasing=true;
        for(int i=0; i<numbers.length-1; i++) // cycling through array
            isIncreasing &= numbers[i] <= numbers[i+1]; // checking if numbers are increasing

        boolean hasAdjacentEqual = numbers[0] == numbers[1];
        for(int pos=0; pos<numbers.length-1; pos++) // cycling through array
            hasAdjacentEqual |= numbers[pos] == numbers[pos+1]; // checking if the next number is equal to current number

        return hasAdjacentEqual && isIncreasing;
    }// END part1()


    public static boolean part2(int input){
        char[] numbers = Integer.toString(input).toCharArray();

        boolean isIncreasing=true;
        for(int i=0; i<numbers.length-1; i++) // cycling through array
            isIncreasing &= numbers[i] <= numbers[i+1]; // checking if numbers are increasing

        boolean hasAdjacentEqual = numbers[0] == numbers[1] && numbers[1] != numbers[2]; // starting out with the fact that if there are 3 consecutive integers next to each other, hasAdjacentEqual <- false
        for(int pos=1; pos<numbers.length-2; pos++)// cycling through array; limiting as it has to check if there are >2 consecutive integers
            hasAdjacentEqual |= numbers[pos] == numbers[pos+1] && numbers[pos+1] != numbers[pos+2] && numbers[pos] != numbers[pos-1]; // checking for >2 consecutive integers
        hasAdjacentEqual |= numbers[4] == numbers[5] && numbers[4] != numbers[3]; // checking the last part of the array

        return hasAdjacentEqual && isIncreasing;
    }// END part2()

}// END