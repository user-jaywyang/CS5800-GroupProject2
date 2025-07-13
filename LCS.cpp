// Abhilash Singh,  Alex Williams,  Jay Yang
// CS5800 - Summer 2025 - Group Project
// Dynamic Programming Problem 2: Longest Common Subsequence (Leetcode 1143)
// This script takes two input strings and returns the Longest Common Subsequence between them

#include "LCS.hpp"

int longestCommonSubsequence(std::string text1, std::string text2) {
    int m = text1.length();
    int n = text2.length();
    std::vector<std::vector<int>> table(m + 1, std::vector<int>(n + 1, 0));

    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (text1[i] == text2[j])
                table[i][j] = 1 + table[i + 1][j + 1];
            else
                table[i][j] = std::max(table[i + 1][j], table[i][j + 1]);
        }
    }

    return table[0][0];
}

