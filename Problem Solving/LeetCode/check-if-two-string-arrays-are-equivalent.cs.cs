// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

bool ArrayStringsAreEqual(string[] word1, string[] word2) {

    StringBuilder text1 = new StringBuilder("");
    StringBuilder text2 = new StringBuilder("");

    foreach(string w1 in word1){
        text1.Append(w1);
    }
    foreach(string w2 in word2){
        text2.Append(w2);
    }

    if (text1.Equals(text2)){
        return true;
    }else{
        return false;
    }
}
