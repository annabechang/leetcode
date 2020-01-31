"""
299. Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""
#Use dictionary
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_dict = collections.defaultdict(int)
        # collections.defaultdict(int):dict subclass that calls a factory function int to supply missing values
        # it assign a defult value usually 0 to it 
        
        for s,g in zip(secret, guess):
            if s == g == 0:
                return
            elif s == g:
                bulls += 1
            else:
                secret_dict[s]+=1
            
        for i,g in enumerate(guess):
            if secret[i]!=guess[i] and secret_dict[g]:
                cows +=1
                secret_dict[g] -=1
        return str(bulls) + "A" +str(cows)+"B"    

"""
Success
Details 
Runtime: 36 ms, faster than 81.25% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
 """
 class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s,g = Counter(secret), Counter(guess)
        A = sum(i==j for i,j in zip(secret, guess))
        return '%sA%sB' % (A, sum((s & g).values())-A)
            
"""
Counter:dict subclass for counting hashable objects
 The %s token allows me to insert (and potentially format) a string. 
 Notice that the %s token is replaced by whatever I pass to the string after the % symbol. 
 Notice also that I am using a tuple here as well (when you only have one string using a tuple is optional) 
 to illustrate that multiple strings can be inserted and formatted in one statement.
"""
"""
 Success
Details 
Runtime: 36 ms, faster than 81.25% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
 """
 
 
 class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g =list(secret),list(guess)
        a,b,i,j=0,0,0,0
    
        while i<len(s):
            if s[i]==g[i]:
                a+=1
                s.remove(s[i])
                g.remove(g[i])
            else:
                i+=1
        
        while j<len(g):
            if g[j] in s:
                s.remove(g[j])
                g.remove(g[j])
                b+=1
            else:
                j+=1
        return str(a)+'A'+str(b)+'B'
"""
we can also use the list to solve this question but the time and memory complexity were much higher than dictionary. 
Success
Details 
Runtime: 72 ms, faster than 9.84% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
"""
 
 
 
 
            
