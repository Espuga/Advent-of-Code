import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner; 

public class day6{
    public static void main(String[] args) {
        ArrayList<String> time = new ArrayList<>();
        ArrayList<String> distance = new ArrayList<>();
        Integer result1 = 1;
        try {
            File myObj = new File("./inputs/input6.txt");
            Scanner reader = new Scanner(myObj);
        
            while (reader.hasNextLine()) {
                String currentData = reader.nextLine();
                String[] data = currentData.split(":");
                if(data[0].equals("Time")) {
                    String[] timeData = data[1].trim().split("\\s+");
                    time.addAll(Arrays.asList(timeData));
                }else {
                    String[] timeData = data[1].trim().split("\\s+");
                    distance.addAll(Arrays.asList(timeData));
                }
            }

            reader.close();
        }catch (FileNotFoundException e){
            System.out.println("ERROR!");
            e.printStackTrace();
        }

        // Part 1
        for(int i = 0; i < time.size(); i++){
            Long segon = Long.parseLong(time.get(i));
            Long metre = Long.parseLong(distance.get(i));

            result1 *= calcular(segon, metre);
        }
        System.out.println("Result 1: "+ result1.toString());

        // Part 2
        Long segon2 = Long.parseLong(String.join(", ", time).replace(", ", ""));
        Long metre2 = Long.parseLong(String.join(", ", distance).replace(", ", ""));

        System.out.println("Result 2: "+ calcular(segon2, metre2).toString());
        
    }

    public static Integer calcular(Long segon, Long metre){
        Integer intents = 0;

        for(int x = 0; x <= segon; x++){
            if((segon-x)*x > metre){
                intents++;
            }
        }

        return intents;
    }
}