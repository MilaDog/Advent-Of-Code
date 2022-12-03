package day2;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day2_part1 {
    public static void main(String[] args) {

        List<Integer> inptVals = readFile("./src/day2/input.txt");

        // Starting of changes
        inptVals.set(1,12);
        inptVals.set(2,2);

        int curr=0;
        int answer=0;
        int stored=0;

        do{
            switch(inptVals.get(curr)){
                case 1:

                    int oC1 = (inptVals.get(inptVals.get(curr+1))) + (inptVals.get(inptVals.get(curr+2)));
                    stored = inptVals.get(curr+3);
                    inptVals.set(stored, oC1);
                    curr = curr+4;
                    answer = inptVals.get(0);

                    break;
                case 2:

                    int oC2 = (inptVals.get(inptVals.get(curr+1))) * (inptVals.get(inptVals.get(curr+2)));
                    stored = inptVals.get(curr+3);
                    inptVals.set(stored,oC2);
                    curr = curr + 4;
                    answer = inptVals.get(0);

                    break;
                case 99:
                    break;
            }
        }while(inptVals.get(curr) != 99);

        System.out.println(answer);

    }// END main

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

}
