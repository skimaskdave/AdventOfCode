import java.io.BufferedReader;
import java.io.FileReader;

public class Day2 {

    public static int getGamePower(String line) {
        String[] parts = line.split(":");
        int blue, red, green;
        blue = 0;
        red = 0;
        green = 0;

        String[] handfuls = parts[1].split(";");
        for (String h : handfuls) {
            h = h.strip();
            String[] colours = h.split(",");
            for (String c : colours) {
                c = c.strip();
                String[] temp = c.split(" ");
                if (temp[1].equals("red")) {
                    if (Integer.parseInt(temp[0]) > red) {
                        red = Integer.parseInt(temp[0]);
                    }
                }
                if (temp[1].equals("green")) {
                    if (Integer.parseInt(temp[0]) > green) {
                        green = Integer.parseInt(temp[0]);
                    }
                }
                if (temp[1].equals("blue")) {
                    if (Integer.parseInt(temp[0]) > blue) {
                        blue = Integer.parseInt(temp[0]);
                    }
                }
            }
        }

        return red * blue * green;
    }

    public static int isValidGame(String line) {
        String[] parts = line.split(":");
        int id = Integer.parseInt(parts[0].split(" ")[1]);

        String[] handfuls = parts[1].split(";");
        for (String h : handfuls) {
            h = h.strip();
            String[] colours = h.split(",");
            for (String c : colours) {
                c = c.strip();
                String[] temp = c.split(" ");
                if (temp[1].equals("red") && Integer.parseInt(temp[0]) > 12) {
                    return 0;
                }
                if (temp[1].equals("green") && Integer.parseInt(temp[0]) > 13) {
                    return 0;
                }
                if (temp[1].equals("blue") && Integer.parseInt(temp[0]) > 14) {
                    return 0;
                }
            }
        }

        return id;
    }

    public static void main(String[] args) {
        BufferedReader reader;
        int validGameCount = 0;
        int mode = Integer.parseInt(args[0]);

        try {
            reader = new BufferedReader(new FileReader("inputs/day2.txt"));
            String line = reader.readLine();
            while (line != null) {
                if (mode == 1) {
                    validGameCount += isValidGame(line);
                }
                else if (mode == 2) {
                    validGameCount += getGamePower(line);
                }
                else {
                    System.out.println(mode + " is not a valid mode");
                    break;
                }
                line = reader.readLine();
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println(validGameCount);

    }
}