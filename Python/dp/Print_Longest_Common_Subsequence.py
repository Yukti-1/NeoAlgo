# Problem Statement -  Print the longest Common Subsequence between two strings.
# _________________________________________________________________________________________________________________
'''
Example Input -
 
    Enter two strings : COMMON DOREMMON

Output - 
    The longest Common Subsequence is OMMON.
'''
# __________________________________________________________________________________________________________________
# Prerequisites :
# 1) Subsequence - A subsequence is a sequence that can be derived from another sequence by removing zero or more
#                  elements, without changing the order of the remaining elements.

# 2) Longest Common Subsequence - A subsequence which is present in both the given Strings i.e. common as well as
#                                 longest among all the common subsequences.
# __________________________________________________________________________________________________________________


def longest_common_subsequence(str1, str2, m, n):
    # Constructing matrix of dimensions [n+1][m+1] where n and m are length of str1 and str2 respectively
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    
    # Filling the value in the dp matrix by traversing it
    # if the character str1[i-1] is equal to str2[j-1] then increment the value dp[i-1][j-1] by 1 and store it at dp[i][j]
    # the value at dp[i][j] store the length of the longest common subsequence for the strings of length i and j.

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    index = dp[m][n]

    longest_common_subsequence = [""] * (index+1)
    longest_common_subsequence[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if str1[i-1] == str2[j-1]:
            longest_common_subsequence[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("Longest Common Subsequence of " + str1 + " and " +
          str2 + " is " + "".join(longest_common_subsequence))


String_1 = input("Enter a string: ")
String_2 = input("Enter another string: ")
m = len(String_1)
n = len(String_2)
longest_common_subsequence(String_1, String_2, m, n)
