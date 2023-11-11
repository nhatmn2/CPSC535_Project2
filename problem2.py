#name: Nathan Nguyen
#email: nhatmn2@csu.fullerton.edu
#class: Mon 7:00pm - 9:45pm

class LongestStringChain:
    def Depth_First_Search(self, i, strings, word_hashmap, memo):
        # If the result for this word is already computed, return it (memoization)
        if i in memo:
            return memo[i]

        # Initialize the maximum length and sequence starting with the current word
        maximum_chain_length = 1
        string_chain = [strings[i]]

        #Iterate over each character in the current strings list
        for j in range(len(strings[i])):
            # Create a predecessor word by removing the j-th character
            predecessor = strings[i][:j] + strings[i][j+1:]
            #if predecessor in word_hashMap then we recursively find the maximum chain length and also the string chain sequence for the predecessor
            if predecessor in word_hashmap:
                current_chain_length, current_string_chain = self.Depth_First_Search(word_hashmap[predecessor], strings, word_hashmap, memo)
                #Update the maximum_chain_length and string_chain if longer than the current maximum
                if current_chain_length + 1 > maximum_chain_length:
                    maximum_chain_length = current_chain_length + 1
                    string_chain = [strings[i]] + current_string_chain
                
		# Store the result in the memo dictionary for memoization
        memo[i] = (maximum_chain_length, string_chain)
        return memo[i]

    def longest_string_chain(self, strings: list[str]) -> list[str]:
        #Sort the words based on their lengths in descending order
        strings.sort(key=lambda w: -len(w))
        word_hashmap = {w: i for i, w in enumerate(strings)}
        
        #result dictionary to store the longest string chain and string sequence
        longest_chain_dict= {} 
        #create a variable to store the longest string chain found 
        longest_chain = []
        
        # Iterate over each word and find the longest chain
        for i in range(len(strings)):
            _, current_chain = self.Depth_First_Search(i, strings, word_hashmap, longest_chain_dict)
            # Update the longest chain if a longer one is found
            if len(current_chain) > len(longest_chain):
                longest_chain = current_chain
        # Return the longest word chain
        return longest_chain
    
def main():
    string_chain = LongestStringChain()
    strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    print(string_chain.longest_string_chain(strings))

if __name__ == "__main__":
    main()

        
        

