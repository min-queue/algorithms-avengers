import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class question {
    public static void main(String[] args) {
//        questionOne("A man, a plan, a canal: Panama");
//        questionTwo();

    }


    public static boolean questionOne(String s) {
        String matchCase = "[^\uAC00-\uD7A3xfe0-9a-zA-Z\\s]";

        s = "A man, a plan, a canal: Panama";

        String toLowerCase = s.toLowerCase();

        String trimWord = toLowerCase.replaceAll("\\s+", "");
        String targetValue = trimWord.replaceAll(matchCase, "");

        int lengthCount = targetValue.length();
        int loopCount = lengthCount;
        int n = 1;
        for (int i = 0; i < lengthCount; i++) {
            if (targetValue.charAt(i) != targetValue.charAt(i + (loopCount - n))) {
                return false;
            }
            loopCount--;
            n++;
        }
        return true;
    }

    public static String[] questionTwo() {
        String[] logs = {"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"};

        Arrays.sort(logs, new MyCompare());

        for (String data : logs) {
            System.out.println(data);
        }
        return logs;
    }

    public static class MyCompare implements Comparator<String> {
        @Override
        public int compare(String log1, String log2) {
            int idx1 = log1.indexOf(" ") + 1;
            int idx2 = log2.indexOf(" ") + 1;

            if (log1.charAt(idx1) >= 'a' && log1.charAt(idx1) <= 'z' &&
                    log2.charAt(idx2) >= 'a' && log2.charAt(idx2) <= 'z') {
                String data1 = log1.substring(idx1);
                String data2 = log2.substring(idx2);

                int compareTo = data1.compareTo(data2);
                if (compareTo != 0) {
                    return compareTo;
                } else {
                    // 에외 처리
                    return log1.compareTo(log2);
                }

            } else if (log1.charAt(idx1) >= 'a' && log1.charAt(idx1) <= 'z') {
                return -1;
            } else if (log2.charAt(idx2) >= 'a' && log2.charAt(idx2) <= 'z') {
                return 1;
            } else {
                return 0;
            }
        }
    }
}
