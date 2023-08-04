
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) -1, -1, -1):
        for w in wordDict:
            #print(w)
            print(dp[i])
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
                print(dp[i]) # For test

            if dp[i]:
                break

    return dp[0]
    
def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    wordBreak(s, wordDict)
    #print(wordBreak(s, wordDict)) // For testing

main()