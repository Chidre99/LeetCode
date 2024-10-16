char * mergeAlternately(char * word1, char * word2) {
    // Get the lengths of the two input strings
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    
    // Allocate memory for the merged string. It needs to hold len1 + len2 characters + 1 for the null terminator
    char *merged = (char *)malloc((len1 + len2 + 1) * sizeof(char));
    
    // Pointers for the merged string and the two input strings
    int i = 0, j = 0, k = 0;
    
    // Alternately merge characters from word1 and word2
    while (i < len1 && j < len2) {
        merged[k++] = word1[i++];
        merged[k++] = word2[j++];
    }
    
    // If there are remaining characters in word1, add them
    while (i < len1) {
        merged[k++] = word1[i++];
    }
    
    // If there are remaining characters in word2, add them
    while (j < len2) {
        merged[k++] = word2[j++];
    }
    
    // Null-terminate the merged string
    merged[k] = '\0';
    
    return merged;
}