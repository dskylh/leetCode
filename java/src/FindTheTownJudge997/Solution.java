package FindTheTownJudge997;

import java.util.Hashtable;

public class Solution {
    public int findJudge(int n, int[][] trust) {
        Hashtable<Integer, Integer> hashMap = new Hashtable<>();
        if (trust.length == n) {
            return -1;
        }
        for (int[] ints : trust) {
            hashMap.put(ints[0], ints[1]);
        }
        for (int i = 1; i <= n; i++) {
            if (!hashMap.containsKey(n)){
                for (int[] ints :
                        trust) {
                    if (ints[1] != n)
                        return -1;
                }
                return n;
                
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        solution.findJudge(4, new int[][]);

    }
}

