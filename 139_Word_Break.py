"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

https://leetcode.com/problems/word-break/solutions/748479/python3-solution-with-a-detailed-explanation-word-break/?orderBy=most_votes&languageTags=python3
dp[i] shows whether subarray s[0:i] is available in the wordDict.

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # have a dp that compare at each position of s if it match with the word in dict. with reverse s order 
        # 
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
            # for w in wordDict:
                # there is enough char in s 
                # and the char is equal
                
                # if  s[i:i+len(w)] == w:
                if (dp[j] and s[j:i]) in wordDict:
                    # if dp at position 0+word
                    # dp[i]== dp[i+len(w)]
                    dp[i]=True
                    print(i,j,dp[j],s[j:i], dp)
                    # break
                # if dp[i] is True:
                #     break #break for loop to next word
                
        return dp[len(s)]
