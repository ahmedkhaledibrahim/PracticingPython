from mailcap import subst
from string import ascii_letters

characters = list(ascii_letters)

def get_frequency(sentence):
    frequencies = [(c,0) for c in characters]
    for letter in sentence:
        index = characters.index(letter)
        frequencies[index] = (letter,frequencies[index][1]+1)
    return frequencies



def mergeAlternately(word1, word2):
    max_length = max(len(word1),len(word2))
    difference = max_length - abs(len(word1) - len(word2))
    i = 0
    result = ""
    while i < max_length:
        if i > 0 and i == difference:
            if len(word1) > len(word2):
                result = result + word1[i::]
                return result
            elif len(word1) < len(word2):
                result = result + word2[i::]
                return result
        result = result + word1[i]+word2[i]
        i +=1
    return result

mergeAlternately("ab","pq")
