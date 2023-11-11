class Solution:
    def dfs(self, i, words, word_index, dp):
        if i in dp:
            return dp[i]

        max_length = 1
        sequence = [words[i]]  # Start with the current word

        for j in range(len(words[i])):
            w = words[i]
            pred = w[:j] + w[j+1:]
            if pred in word_index:
                current_length, current_sequence = self.dfs(word_index[pred], words, word_index, dp)
                if current_length + 1 > max_length:
                    max_length = current_length + 1
                    sequence = [w] + current_sequence

        dp[i] = (max_length, sequence)
        return dp[i]

    def longestStrChain(self, words: list[str]) -> list[str]:
        words.sort(key=lambda w: -len(w))
        word_index = {w: i for i, w in enumerate(words)}
        dp = {}

        longest_chain = []
        for i in range(len(words)):
            _, current_chain = self.dfs(i, words, word_index, dp)
            if len(current_chain) > len(longest_chain):
                longest_chain = current_chain

        return longest_chain

# Example usage
sol = Solution()
words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(sol.longestStrChain(words))  # It will print the longest chain of words