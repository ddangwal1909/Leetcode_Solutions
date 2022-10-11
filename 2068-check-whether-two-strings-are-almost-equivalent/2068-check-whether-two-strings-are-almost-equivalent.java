class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
     
        int arr[] = new int[26];
        int arr1[] = new int[26];
        
        for(int i=0;i<word1.length();i++){
            arr[(int)word1.charAt(i) - (int)('a')]+=1;
        }
        
        for(int i=0;i<word2.length();i++){
            arr1[(int)word2.charAt(i) - (int)('a')]+=1;
        }
        
        for(int i=0;i<26;i++){
            if (Math.abs(arr[i]-arr1[i])>3){
                return false;
            }
        }
        
        return true;
        
        
    }
}