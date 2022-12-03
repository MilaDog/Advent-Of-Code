package day2;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day2_part2 {

    static List<Integer> inptArr = readFile("./src/day2/input.txt");

    public static void main(String[] args) {

        int result = part2();
        System.out.println(result);

    }

    static int part2(){
        int answer=0;

        for(int noun=0;noun<=99;noun++)
            for (int verb=0; verb<=99;verb++) {
                List<Integer> inptNew = new ArrayList<Integer>(inptArr);

                if (part1(inptNew,noun,verb) == 19690720) // checking if the value at index 0 == 19690720
                    answer = (100*noun)+verb;

            }
        return answer;
    }


    static int part1(List<Integer> arr, int noun, int verb){

        arr.set(1,noun);
        arr.set(2,verb);

        int curr = 0;

        do {
            switch (arr.get(curr)) {
                case 1:

                    int oC1 = (arr.get(arr.get(curr + 1))) + (arr.get(arr.get(curr + 2))); // Getting value at x-index, then that value used to get the value of y-index (for both)
                    arr.set(arr.get(curr + 3), oC1); // getting the value of the index 3 indexes after the opCode, and replacing with the sum of above
                    curr += 4; // increasing position by 4

                    break;
                case 2:

                    int oC2 = (arr.get(arr.get(curr + 1))) * (arr.get(arr.get(curr + 2))); // Getting value at x-index, then that value used to get the value of y-index (for both)
                    arr.set(arr.get(curr + 3), oC2); // getting the value of the index 3 indexes after the opCode, and replacing with the product of above
                    curr += 4; // increasing position by 4

                    break;
                case 99: // ending after 99 is found
                    break;
                default:
                    System.out.println("Error");
                    break;
            }
        }while (arr.get(curr) != 99); //Ending do-while

        return arr.get(0); // returning value at index 0
    }


    public static List<Integer> readFile(String loc){
        List<Integer> inptVals = new ArrayList<>();
        try{
            Scanner scnFile = new Scanner(new File(loc)).useDelimiter(",");

            int val=0;
            while(scnFile.hasNextInt()){
                val = scnFile.nextInt();
                inptVals.add(val);
            }
            scnFile.close();

        }catch(FileNotFoundException err){
            err.printStackTrace();
        }
        return inptVals;
    }// END readFile()

}// END
