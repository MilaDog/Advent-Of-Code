package day3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class day3 {
    public static void main(String[] args) {
        part1(readFile("./src/day3/input.txt"));
    }// END main

    public static void part1(List<String> input){

        HashMap<String, Integer> wire1 = calcManDis(input.get(0));
        HashMap<String, Integer> wire2 = calcManDis(input.get(1));

        wire1.keySet().retainAll(wire2.keySet());

        int min = Integer.MAX_VALUE;
        int minSteps = Integer.MAX_VALUE;

        for(String el: wire1.keySet()){ // getting [x;y] coords for each incept, then calculating the Manhattan distance from the origin
            int x = (Integer.parseInt(el.split(";")[0]));
            int y = (Integer.parseInt(el.split(";")[1]));
            int dis = Math.abs(x) + Math.abs(y);

            // Getting smallest Manhattan distance from origin
            if(dis < min)
                min = dis;
            // Getting steps
            int r = part2(input,x,y);
            if(r < minSteps)
                minSteps = r;
        }// END loop -> common intercepts

        System.out.println("Distance: " + min);
        System.out.println("Steps [smallest / to first intercept]: " + minSteps);

    }// END part1()

    public static HashMap<String, Integer> calcManDis(String input){
        HashMap<String, Integer> grid = new HashMap<>();

        String[] instructions = input.split(",");
        int x=0;
        int y=0;
        int amt=0;
        for(String action: instructions){
            // Get the direction of movement
            if(action.startsWith("R"))
                amt = Integer.parseInt(action.substring(1));
            if(action.startsWith("L"))
                amt = Integer.parseInt(action.substring(1));
            if(action.startsWith("U"))
                amt = Integer.parseInt(action.substring(1));
            if(action.startsWith("D"))
                amt = Integer.parseInt(action.substring(1));

            for(int i=0; i<amt; i++){ // getting coords of each move
                if(action.startsWith("R"))
                    x++;
                else if(action.startsWith("L"))
                    x--;
                else if(action.startsWith("U"))
                    y++;
                else if(action.startsWith("D"))
                    y--;

                String coord = String.format("%d;%d",x,y);
                grid.put(coord, 1);
            }// END loop -> distance moved
        }// END loop -> each element in array
        return grid;
    }// END part1()


    public static int part2(List<String> input, int fx, int fy){
        int steps=0;
        for(String wire: input) {
            String[] instructions = wire.split(",");
            int x = 0;
            int y = 0;
            int amt = 0;
            boolean flag = false;
            for (String action : instructions) {
                if (flag) break;
                // Get the direction of movement
                if (action.startsWith("R"))
                    amt = Integer.parseInt(action.substring(1));
                if (action.startsWith("L"))
                    amt = Integer.parseInt(action.substring(1));
                if (action.startsWith("U"))
                    amt = Integer.parseInt(action.substring(1));
                if (action.startsWith("D"))
                    amt = Integer.parseInt(action.substring(1));

                for (int i = 0; i < amt; i++) { // getting coords of each move
                    if (action.startsWith("R"))
                        x++;
                    else if (action.startsWith("L"))
                        x--;
                    else if (action.startsWith("U"))
                        y++;
                    else if (action.startsWith("D"))
                        y--;
                    steps++;
                    if (fx == x && fy == y) {
                        flag = true;
                        break;
                    }
                }// END loop -> distance moved
            }// END loop -> each element in array
        }// END loop wire
        return steps;
    }// END part2()


    public static List<String> readFile(String filePath){
        List<String> arr = new ArrayList<>();
        BufferedReader reader;

        try{
            File file = new File(filePath);
            reader = new BufferedReader(new FileReader(file));
            String line = reader.readLine();

            while(line != null){
                arr.add(line);
                line = reader.readLine();
            }
            reader.close();

        }catch(IOException err){
            err.printStackTrace();
        }
        return arr;
    }// END readFile()

}// END
