package day1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class day1 {
    public static void main(String[] args) {
        String loc = "./src/day1/input.txt";
        part1(readFile(loc));
    }// END main


    public static void part1(List<String> input){
        List<Integer> arr = input.stream().map(Integer::valueOf).collect(Collectors.toList());

        int fuelP1=0;
        int fuelP2=0;
        for(Integer fuel: arr){
            fuelP1 += ((fuel/3)+2);
            fuelP2 += part2(fuel);
        }// END loop
        System.out.println(fuelP1);
        System.out.println(fuelP2);
    }// END part1()


    public static int part2(int input){

        int total=0;
        while(input > 0){
            int result = (input/3)+2;

            if(result>0)
                total+= result;
            input= result;
        }
        return total;
    }// END part2()


    public static List<String> readFile(String fileLocation){
        List<String> arr = new ArrayList<>();
        BufferedReader reader;

        try{
            File file = new File(fileLocation);
            reader = new BufferedReader(new FileReader(file));

            String line = reader.readLine();
            while(line != null){
                arr.add(line);
                line = reader.readLine();
            }
            reader.close();
        }catch(IOException err){
            err.printStackTrace();
        }// END try-catch
        return arr;
    }// END readFile()

}// END
