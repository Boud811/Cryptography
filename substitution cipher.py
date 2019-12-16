import string
import random



def generate_key():
    dic = {}
    S = [i for i in range (0,26)]
    for i in range(26):
        k = random.randint(0, 25-i)
        assigned_letter = string.ascii_uppercase[S[k]]
        letter_to_assign = string.ascii_uppercase[i]
        d = {letter_to_assign:assigned_letter}
        dic.update(d) 
        S.pop(k)  
    return dic
dic = generate_key()


def splitter(text, word_size = 5):
    """[splits the input into words of the specified length]
    
    Arguments:
        text {string} -- [what you want to seperate]
    
    Keyword Arguments:
        word_size {int} -- [the length of each word] (default: {5})
    
    Returns:
        [string] -- [description]
    """    
    text.strip(" ")
    counter = 0
    modified_text = ""
    for letter in text:
        counter = (counter +1)
        if counter % word_size == 0: 
            modified_text = modified_text +text[counter-word_size:counter] + " "

    return modified_text
def Substitution_encryption(plain_text, key):
    """[it encrypts the text and outputs it into the usual format (5 - letters words)]

    Arguments:
        plain_text {[string]} -- [the text you want to encrypt]
        key {[dict]} -- [the rule of encryption]
    """    
    plain_text = plain_text.upper()
    cipher_text = ""
    for letter in plain_text:
        if letter in string.punctuation or letter == " ":
            pass
        else:
            l = key[letter] 
            cipher_text = cipher_text + l
    return splitter(cipher_text)

    
def Substitution_decryption(cipher_text, key):
    """[it decrypts the cipher text and outputs it into the usual format (5 - letters words)]

    Arguments:
        cipher_text {[string]} -- [the text you want to encrypt]
        key {[dict]} -- [the rule of encryption]
    """    

    
    key = dict([[v,k]for k,v in key.items()])
    decrypted_text =""
    for letter in cipher_text:
        if letter in string.punctuation or letter == " ":
            pass
        else:
            l = key[letter] 
            decrypted_text = decrypted_text + l
    return splitter(decrypted_text)

























print(Substitution_encryption("The problem of distinguishing prime numbers from composite numbers and of resolving the latter into their prime factors is known to be one of the most important and useful in arithmetic. It has engaged the industry and wisdom of ancient and modern geometers to such an extent that it would be superfluous to discuss the problem at length... Further, the dignity of the science itself seems to require that every possible means be explored for the solution of a problem so elegant and so celebrated.", dic),dic)