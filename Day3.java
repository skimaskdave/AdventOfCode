import java.io.BufferedReader;
import java.io.FileReader;

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
        System.out.println("Not implemented yet");
        return 0;
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
