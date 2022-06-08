# Pozdravujem Maroška
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def atbash(txt):
    phrase = ""
    for i in txt:
        if i.isalpha():
            if i.isupper():
                phrase += alphabet_upper[len(alphabet_upper) - alphabet_upper.index(i) - 1]
            else:
                phrase += alphabet_lower[len(alphabet_lower) - alphabet_lower.index(i) - 1]
        else:
            phrase += i
    return(phrase)
