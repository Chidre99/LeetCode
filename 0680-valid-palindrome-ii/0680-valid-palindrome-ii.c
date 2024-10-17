// Helper function to check if a substring is a palindrome
bool isPalindrome(char* s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// Main function to check if the string is a valid palindrome
bool validPalindrome(char* s) {
    int left = 0;
    int right = strlen(s) - 1;

    // Use two pointers to check if the string is a palindrome
    while (left < right) {
        if (s[left] != s[right]) {
            // If there's a mismatch, try removing one character and check if the rest is a palindrome
            return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1);
        }
        left++;
        right--;
    }
    return true; // If no mismatches, it's a palindrome
}
