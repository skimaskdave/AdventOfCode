import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day1 {

    public static int sumValues(int[] values) {
        int calibrationValues;
        if (values[1] == -1) {
            calibrationValues = values[0] * 10 + values[0];
        }
        else {
            calibrationValues = values[0] * 10 + values[1];
        }
        return calibrationValues;
    }

    public static int calculateCalibrationValuesWithStrings(String line) {
        int calibrationValues = 0;
        boolean front, back;
        int[] values = {-1, -1};
        ArrayList<Integer> indexes = new ArrayList<>();

        front = false;
        back = false;

        for (int i=0; i<line.length(); i++) {
            if (line.charAt(i) >= '0' && line.charAt((i)) <= '9') {
                indexes.add(i);
            }
        }

        for (int i=0; i<indexes.size(); i++) {
            // if we need to check for words at the front
            if ((int) indexes.get(i) < 3) {
                front = true;
            }
            // if we need to check for words at the back
            else if ((int) indexes.get(i) > line.length()-3) {
                back = true;
            }
        }

        int minIndex = 10000;
        for (int i=0; i<indexes.size(); i++) {
            if ((int) indexes.get(i) < minIndex) {
                minIndex = indexes.get(i);
            }
        }

        int maxIndex = -1;
        for (int i=0; i<indexes.size(); i++) {
            if ((int) indexes.get(i) > maxIndex) {
                maxIndex = indexes.get(i);
            }
        }
        if (!front) {
            for (int i=0; i<minIndex; i++) {
                if (i+3 <= minIndex) {
                    if (line.substring(i, i+3).equals("one")) {
                        values[0] = 1;
                        break;
                    }
                    else if (line.substring(i, i+3).equals("two")) {
                        values[0] = 2;
                        break;
                    }
                    else if (line.substring(i, i+3).equals("six")) {
                        values[0] = 6;
                        break;
                    }
                }
                if (i+4 <= minIndex) {
                    if (line.substring(i, i+4).equals("four")) {
                        values[0] = 4;
                        break;
                    }
                    else if (line.substring(i, i+4).equals("five")) {
                        values[0] = 5;
                        break;
                    }
                    else if (line.substring(i, i+4).equals("nine")) {
                        values[0] = 9;
                        break;
                    }
                }
                if (i+5 <= minIndex) {
                    if (line.substring(i, i+5).equals("three")) {
                        values[0] = 3;
                        break;
                    }
                    else if (line.substring(i, i+5).equals("seven")) {
                        values[0] = 7;
                        break;
                    }
                    else if (line.substring(i, i+5).equals("eight")) {
                        values[0] = 8;
                        break;
                    }
                }
            }
            if (values[0] == -1) {
                values[0] = line.charAt(minIndex) - '0';
            }
        }
        else {
            values[0] = line.charAt(minIndex) - '0';
        }

        if (!back) {
            for (int i=line.length(); i>maxIndex; i--) {
                if (i-3 >= maxIndex && i-3 >= 0) {
                    if (line.substring(i-3, i).equals("one")) {
                        values[1] = 1;
                        break;
                    }
                    else if (line.substring(i-3, i).equals("two")) {
                        values[1] = 2;
                        break;
                    }
                    else if (line.substring(i-3, i).equals("six")) {
                        values[1] = 6;
                        break;
                    }
                }
                if (i-4 >= maxIndex && i-4 >= 0) {
                    if (line.substring(i-4, i).equals("four")) {
                        values[1] = 4;
                        break;
                    }
                    else if (line.substring(i-4, i).equals("five")) {
                        values[1] = 5;
                        break;
                    }
                    else if (line.substring(i-4, i).equals("nine")) {
                        values[1] = 9;
                        break;
                    }
                }
                if (i-5 >= maxIndex && i-5 >= 0) {
                    if (line.substring(i-5, i).equals("three")) {
                        values[1] = 3;
                        break;
                    }
                    else if (line.substring(i-5, i).equals("seven")) {
                        values[1] = 7;
                        break;
                    }
                    else if (line.substring(i-5, i).equals("eight")) {
                        values[1] = 8;
                        break;
                    }
                }
            }
            if (values[1] == -1) {
                values[1] = line.charAt(maxIndex) - '0';
            }
        }
        else {
            values[1] = line.charAt(maxIndex) - '0';
        }

        return sumValues(values);
    }

    public static int calculateCalibrationValues(String line) {
        int[] values = {-1, -1};

        for (int i=0; i<line.length(); i++) {
            if (line.charAt(i) >= '0' && line.charAt((i)) <= '9') {
                if (values[0] == -1) {
                    values[0] = line.charAt(i) - '0';
                } else {
                    values[1] = line.charAt(i) - '0';
                }
            }
        }

        return sumValues(values);
    }

    public static void main(String[] args) {
        BufferedReader reader;
        int calibrationSum = 0;
        int mode = Integer.parseInt(args[0]);

        try {
            reader = new BufferedReader(new FileReader("inputs/day1.txt"));
            String line = reader.readLine();
            while (line != null) {
                if (mode == 1) {
                    calibrationSum += calculateCalibrationValues(line);
                }
                else if (mode == 2) {
                    calibrationSum += calculateCalibrationValuesWithStrings(line);
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

        System.out.println(calibrationSum);

    }

}
