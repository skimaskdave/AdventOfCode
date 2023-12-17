import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day3 {

    public static int checkAdjacent(String[] lines) {
        String lnBf = "............................................................................................................................................";
        String lnAf = "............................................................................................................................................";
        String num = "";
        boolean isPartNumber = false;
        int partsSum = 0;
        for (int i=0; i<lines.length; i++) {
            if (i < 139) {
                lnAf = lines[i+1];
            }
            else {
                lnAf = "............................................................................................................................................";
            }
            for (int j=0; j<lines[i].length(); j++) {
                if ((int) lines[i].charAt(j) <= 57 && (int) lines[i].charAt(j) >= 48) {
                    num += lines[i].charAt(j);
                    if (!isPartNumber) {
                        if (j>0) { // check char diagonal left / left of number
                            if ((lnBf.charAt(j-1) != '.') && ((int) lnBf.charAt(j-1) > 57 || (int) lnBf.charAt(j-1) < 48)) {
                                isPartNumber = true;
                            }
                            if ((lnAf.charAt(j-1) != '.') && ((int) lnAf.charAt(j-1) > 57 || (int) lnAf.charAt(j-1) < 48)) {
                                isPartNumber = true;
                            }
                            if ((lines[i].charAt(j-1) != '.') && ((int) lines[i].charAt(j-1) > 57 || (int) lines[i].charAt(j-1) < 48)) {
                                isPartNumber = true;
                            }
                        }
                        if (j<lines[i].length()-1) { // check char diagonal right / right of number
                            if ((lnBf.charAt(j+1) != '.') && ((int) lnBf.charAt(j+1) > 57 || (int) lnBf.charAt(j+1) < 48)) {
                                isPartNumber = true;
                            }
                            if ((lnAf.charAt(j+1) != '.') && ((int) lnAf.charAt(j+1) > 57 || (int) lnAf.charAt(j+1) < 48)) {
                                isPartNumber = true;
                            }
                            if ((lines[i].charAt(j+1) != '.') && ((int) lines[i].charAt(j+1) > 57 || (int) lines[i].charAt(j+1) < 48)) {
                                isPartNumber = true;
                            }
                        }
                        // check char above & below number
                        if ((lnBf.charAt(j) != '.') && ((int) lnBf.charAt(j) > 57 || (int) lnBf.charAt(j) < 48)) {
                            isPartNumber = true;
                        }
                        if ((lnAf.charAt(j) != '.') && ((int) lnAf.charAt(j) > 57 || (int) lnAf.charAt(j) < 48)) {
                            isPartNumber = true;
                        }
                    }
                }
                else {
                    if (isPartNumber) {
                        System.out.println(num);
                        partsSum += Integer.valueOf(num);
                    }
                    isPartNumber = false;
                    num = "";
                }
            }
            lnBf = lines[i];
        }
        return partsSum;
    }

    public static int checkGears(String[] lines) {
        String lnBf = "............................................................................................................................................";
        String lnAf = "............................................................................................................................................";
        ArrayList<Integer> potentialGearLines = new ArrayList<Integer>();
        ArrayList<Integer> potentialGearIndexes = new ArrayList<Integer>();
        ArrayList<String[]> maps = new ArrayList<String[]>();
        String[] nums = {"", ""};
        boolean isPartNumber = false;
        boolean[] posFlags = new boolean[4];
        int partsSum = 0;
        // find all the positions in the file of the gears
        for (int i=0; i<lines.length; i++) {
            for (int j=0; j<lines[i].length(); j++) {
                if (lines[i].charAt(j) == '*') {
                    potentialGearIndexes.add(j);
                    potentialGearLines.add(i);
                }
            }
        }
        // generate a (2-3)*(4-7) 'input' around the gear
        for (int i=0; i<potentialGearLines.size(); i++) {
            int startI, length, startL, height;
            height = 3;
            length = 7;
            startI = potentialGearIndexes.get(i)-3;
            startL = potentialGearLines.get(i)-1;
            // cases where the matrix will be 2 * n
            if (potentialGearLines.get(i) == 0) {
                height = 2;
                startL = 0;
            }
            else if (potentialGearLines.get(i) == lines.length) {
                height = 2;
                startL = lines.length-1;
            }
            // cases where the matrix will be n * (4-7)
            if (potentialGearIndexes.get(i) < 3) {
                startI = 0;
                length = 7-3+potentialGearIndexes.get(i);
            }
            else if (potentialGearIndexes.get(i) > lines[0].length()-3) {

            }
        }
        // count number of adjacent numbers
        // calculate gear ratio
        return partsSum;
    }

    public static void main(String[] args) {
        BufferedReader reader;
        int mode = Integer.parseInt(args[0]);
        String[] lines = new String[140];
        int count = 0;

        try {
            reader = new BufferedReader(new FileReader("inputs/day3.txt"));
            String line = reader.readLine();
            while (line != null) {
                lines[count] = line;
                count++;
                line = reader.readLine();
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        if (mode==1) {
            System.out.println(checkAdjacent(lines));
        }
        else if (mode==2) {
            System.out.println(checkGears(lines));
        }
        else {
            System.out.println("Not a valid mode.");
        }

    }

}
