def LongestWord(sen):
    words = sen.split()
    
    longest_word = ""
    max_length = 0
    
   
    for word in words:
        
        cleaned_word = ''.join(filter(str.isalnum, word))
        
        
        if len(cleaned_word) > max_length:
            longest_word = cleaned_word
            max_length = len(cleaned_word)
    
    return longest_word

print(LongestWord(input()))