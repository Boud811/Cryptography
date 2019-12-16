import collections
import string
MOST_FREQUENT_LETTERS = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']


def frequency_table(cipher_text):
    """[it outputs a frequency table of how much every letter has occurd]

    Arguments:
        cipher_text {[string]} -- [The encrypted text]
    """ 
    m = list(cipher_text)
    frequency_table = []
    for letter in string.ascii_uppercase: 
        frequency_table.append([letter, m.count(letter)])
    table = dict(frequency_table)
    frequency_table =sorted (table.items(), key= lambda kv:[kv[1], kv[0]])
    frequency_table.reverse()
         

    return frequency_table


def pairs_from_text(text):
    text = text.replace(" ", "")
    for index, item in enumerate(text):
        try:
            yield item, text[index + 1]
        except IndexError:
            return



cipher_text = 'VQASF XCHAY XUIGP VGETB GPQGE TSFGY AEBYC AFPUF XYNXY SXPGV AEBYC AFPRE IXUFA PXHZG ETVQA HRVVA FGEVX VQAGF SFGYA URNVX FPGPL EXJEV XCAXE AXUVQ AYXPV GYSXF VREVR EIBPA UBHGE RFGVQ YAVGN GVQRP AETRT AIVQA GEIBP VFMRE IJGPI XYXUR ENGAE VREIY XIAFE TAXYA VAFPV XPBNQ REAWV AEVVQ RVGVJ XBHIC APBSA FUHBX BPVXI GPNBP PVQAS FXCHA YRVHA ETVQU BFVQA FVQAI GTEGV MXUVQ APNGA ENAGV PAHUP AAYPV XFAKB GFAVQ RVAZA FMSXP PGCHA YAREP CAAWS HXFAI UXFVQ APXHB VGXEX URSFX CHAYP XAHAT REVRE IPXNA HACFR'

def strip(text):
    text = text.replace(" ", "")
    text = text.replace(",", '')
    text = text.replace("[", '')
    text = text.replace("]", '')
    text = text.replace("'", '')
    text = text.replace("\"", '')


    return text

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
def show(cipher_text):
    for i in range(len(cipher_text)):
        if cipher_text[i].isupper():
            text = list(cipher_text)

            text[i]="-"
            cipher_text = str(text)
            cipher_text = strip(cipher_text)
            cipher_text = splitter(cipher_text)
    return cipher_text
def pairs_frequency(cipher_text, top):

    pairs = pairs_from_text(cipher_text)
    counter = collections.Counter(pairs)
    pairs_table =sorted (counter.items(), key= lambda kv:[kv[1], kv[0]])
    pairs_table.reverse()
    return pairs_table[:top]

print(frequency_table(cipher_text))
print(pairs_frequency(cipher_text,10))
x = 1
keys =[]
while x != -1:
    x = input("what do you want to replace? \n")
    y = input("what do you want to replace it by? \n")        
    for i in range(len(cipher_text)):
        try:
            if cipher_text[i] == x.upper():
                text = list(cipher_text)

                text[i]=y.lower()
                cipher_text = str(text)
                cipher_text = strip(cipher_text)
                cipher_text = splitter(cipher_text)
            
        except IndexError:
            continue
    
       
    print("----------------\n", cipher_text,"\n----------------\n",show(cipher_text) )
    keys.append ([x,y])


print(keys)
    