
class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s):1}

        def dfs(i):
            # i is position in s
            if i in dp: 
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i+1)    
            print(res)

            if (i+1) < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                res+= dfs(i+2)
                print(res)
            dp[i] = res
            return res
        return dfs(0)

